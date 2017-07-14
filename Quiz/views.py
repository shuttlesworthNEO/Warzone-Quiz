# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Registration.models import UserModel
from models import QuestionModel, ValidationModel
from forms import QuestionForm
from Registration.views import check_validation
from forms import QuestionForm
from django.db.models import Q
# Create your views here.

def QuestionView(request):
    user = check_validation(request)
    if user:
        if user.count <= 3:
            question = QuestionModel.objects.order_by('?')[:1].first()

            print question
            test = ValidationModel.objects.complex_filter(Q(user=user) & Q(question=question))
            while test.exists():
                question = QuestionModel.objects.order_by('?')[:1].first()
                test = ValidationModel.objects.complex_filter(Q(user=user) & Q(question=question))

            new = ValidationModel(user=user, question=question)
            new.save()
            user.count += 1
            user.save()
            return render(request, 'quiz.html', {'question':question})
        else:
            return redirect('/endquiz/')
    else:
        return redirect('/login/')

def CheckAnswerView(request):
    user = check_validation(request)
    if user and request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            print request.body
            response = form.cleaned_data.get('answer')
            ques_response = form.cleaned_data.get('question')
            question = QuestionModel.objects.filter(id=ques_response).first()
            answer = question.answer
            print answer, response
            if answer == response:
                user.score += 1
                user.save()
        return redirect('/quiz/')
    else:
        return redirect('/login/')

def FinalView(request):
    user = check_validation(request)
    if user:
        score = user.score
        return render(request, 'final.html', {'score':score})
    else:
        return redirect('/login/')