from django import forms
from task.models import TaskModel


class TaskModalForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['is_completed']
        