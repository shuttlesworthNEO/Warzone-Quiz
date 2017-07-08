from django import forms
from models import QuestionModel, AnswerModel

class QuestionForm(forms.ModelForm):
    answer = forms.CharField(max_length=5)
    class Meta:
        model = AnswerModel
        fields=['answer', 'question',]