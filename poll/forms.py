from django import forms
from .models import PollModel


class PollModelForm(forms.ModelForm):
    class Meta:
        model = PollModel
        fields = ['question', 'option_one', 'option_two', 'option_three']
