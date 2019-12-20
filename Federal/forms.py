from django import forms
from .models import Executive, Judiciary, Legislative


class ExecutiveCreate(forms.ModelForm):
    class Meta:
        model = Executive
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']


class JudiciaryForm(forms.ModelForm):
    class Meta:
        model = Judiciary
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']


class LegislativeForm(forms.ModelForm):
    class Meta:
        model = Legislative
        fields = '__all__'
        exclude = ['author', 'last_modified_by', 'timestamp']
