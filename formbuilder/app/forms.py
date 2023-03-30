from django import forms
from .models import Form

class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('name',)
