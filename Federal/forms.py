from django import forms
from .models import Executive


class ExecutiveCreate(forms.ModelForm):
    class Meta:
        model = Executive
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']

