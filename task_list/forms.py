from django import forms
from tempus_dominus.widgets import DatePicker
from taggit.forms import TagField, TagWidget
from task_list.models import Task

STATUS_CHOICES = [
    ('done', 'done'),
    ('in progress', 'in progress')
]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-6', 'name': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-6', 'name': 'description', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control col-3', 'name': 'status'}, choices=STATUS_CHOICES),
            'due_date': forms.DateInput(attrs={'class': 'form-control  col-3', 'id': 'myDate', 'type': 'date', 'name': 'myDate'}),
            'tags': TagWidget(attrs={'class': 'form-control col-6'}),

        }
