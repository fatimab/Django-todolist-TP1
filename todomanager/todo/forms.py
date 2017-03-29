from django import forms
from todo.models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')

class TaskDeleteForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = ('__all__')