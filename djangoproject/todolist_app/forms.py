from django import forms
from todolist_app.models import tasklist

class taskform(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task','done']