from django import forms
from models import QuestionModel, ValidationModel

class QuestionForm(forms.Form):
    answer = forms.CharField(max_length=5)
    question = forms.IntegerField()
    fields=['answer', 'question',]