from django import forms
from .models import Event,Results


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'



class EventForm(forms.ModelForm):
    # # date = forms.DateField(widget=forms.DateInput)
    # time = forms.TimeField(widget=forms.TimeInput)

    class Meta:
        model=Event
        fields = ['type', 'name', 'date', 'time', 'description', 'team_A', 'team_B', 'venue']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Event name'},),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'team_A': forms.TextInput(attrs={'placeholder': 'Team A'}),
            'team_B': forms.TextInput(attrs={'placeholder': 'Team B'}),
            'venue': forms.TextInput(attrs={'placeholder': 'Venue'}),
            'date':DateInput(),
            'time':TimeInput(),
        }


class WinnerForm(forms.ModelForm):
    class Meta:
        model=Results
        fields = '__all__'