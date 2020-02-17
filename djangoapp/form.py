from django import forms
from djangoapp.models import Details

class DetailForm(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"