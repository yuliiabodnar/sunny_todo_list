from django import forms
from tasks.models.task import Task
from locations.models.location import Location


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'location', 'completed', 'temperature', 'is_rain', 'is_cloudy', 'is_sunny']

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select,
        empty_label="Select a location",
    )

    temperature = forms.CharField(widget=forms.HiddenInput(), required=False)
    is_rain = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
    is_cloudy = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
    is_sunny = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)

