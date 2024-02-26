from django import forms
from django.forms.widgets import NumberInput

from .models import Logger

SHIFTS = (
    ("1", "Swing"),
    ("2", "Straight Day"),
    ("3", "Grave")
)

MATERIALS = (
    ("1", "PET Coke"),
    ("2", "Alumina"),
    ("3", "RFO"),
    ("4", "Scraps"),
    ("5", "Burn-offs")
)

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
    shift = forms.ChoiceField(choices = SHIFTS)
    materials = forms.ChoiceField(widget=forms.RadioSelect, choices=MATERIALS)