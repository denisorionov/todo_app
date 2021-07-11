

import csv

from django.http import HttpResponse
from django.shortcuts import redirect

from task_list.models import Task


def export_csv(request):
    tasks = Task.objects.all().values_list("id", "title", "description", "due_date", "status")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;    filename="tasks.csv"'
    writer = csv.writer(response)
    writer.writerow(["id", "Title", "Description", "Due date", "Status"])

    for task in tasks:
        writer.writerow(task)

    return response

