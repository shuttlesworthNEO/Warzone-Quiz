from django import forms

class QuestionForm(forms.Form):
    answer = forms.CharField(max_length=5)
    question = forms.IntegerField()
    timer = forms.IntegerField()
    fields=['answer', 'question', 'timer',]