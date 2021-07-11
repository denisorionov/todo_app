from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from task_list.utils import export_csv
from task_list.views import MainView, TaskApi, TaskView, CompletedTasksView, NewTaskView, CurrentTasksView, \
    TaskDetailApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_view'),
    path('tag_filter/<str:tag_filter>/', MainView.as_view(), name='main_view_by_tag'),
    path('api/', TaskApi.as_view()),
    path('api_detail/<int:id>/', TaskDetailApi.as_view()),
    path('task/<int:id>/', TaskView.as_view()),
    path('completed/', CompletedTasksView.as_view()),
    path('current/', CurrentTasksView.as_view()),
    path('new_task/', NewTaskView.as_view()),
    path('export_csv/', export_csv, name='export_csv'),

]
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
