import csv
import io
from datetime import datetime

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from taggit.models import Tag

from task_list.forms import TaskForm
from task_list.models import Task
from task_list.serializers import TaskSerializer


class MainView(View):
    def get(self, request, tag_filter=None):
        tasks = Task.objects.all()
        if tag_filter:
            tag = get_object_or_404(Tag, slug=tag_filter)
            tasks = tasks.filter(tags__in=[tag])
            return render(request, 'task_list/index.html', context={"tasks": tasks})
        return render(request, 'task_list/index.html', context={"tasks": tasks, "main": True})

    def post(self, request):
        csv_file = request.FILES.get('csv_file', False)
        if csv_file:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for row in csv.reader(io_string, delimiter=';', quotechar='"'):
                try:
                    Task.objects.get_or_create(
                        title=row[0],
                        description=row[1],
                        due_date=datetime.strptime(row[2], '%d.%m.%Y'),
                        status=row[3]
                    )
                except ValueError:
                    break
        return redirect('/')


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', '')
        tasks = Task.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return render(request, 'task_list/index.html', context={'tasks': tasks})


class CurrentTasksView(View):
    def get(self, request):
        tasks = Task.objects.filter(status="in progress")
        return render(request, 'task_list/index.html', context={"tasks": tasks})


class CompletedTasksView(View):
    def get(self, request):
        tasks = Task.objects.filter(status="done")
        return render(request, 'task_list/index.html', context={"tasks": tasks})


class TaskView(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        task_form = TaskForm(instance=task)
        return render(request, 'task_list/task_view.html', context={'task_form': task_form, 'change': True})

    def post(self, request, id):
        task = Task.objects.get(id=id)
        if 'save' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            if task_form.is_valid():
                task_form.save()
                return redirect('/')
        elif 'delete' in request.POST:
            task.delete()
            return redirect('/')

        return render(request, 'task_list/task_view.html', context={'task_form': task_form, 'change': True})


class NewTaskView(View):
    def get(self, request):
        task_form = TaskForm()
        return render(request, 'task_list/task_view.html', context={'task_form': task_form})

    def post(self, request):
        if 'create' in request.POST:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_form.save()
        return redirect('/')


class TaskApi(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            Task.objects.get_or_create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                due_date=serializer.validated_data['due_date'],
                status=serializer.validated_data['status']
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            Task.objects.filter(pk=request.data['id']).update(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                due_date=serializer.validated_data['due_date'],
                status=serializer.validated_data['status']
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailApi(APIView):
    def get_task(self, id):
        try:
            task = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            raise Http404
        return task

    def get(self, request, id):
        serializer_task = TaskSerializer(self.get_task(id))
        return Response(serializer_task.data)

    def delete(self, request, id):
        self.get_task(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
