from django import forms
from tasks.models.task import Task
from locations.models.location import Location


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'location', 'completed']
        location = forms.ModelChoiceField(
            queryset=Location.objects.all(),
            widget=forms.Select,
            empty_label="Select a location",
        )
