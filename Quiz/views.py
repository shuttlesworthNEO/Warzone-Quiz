# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from Registration.models import UserModel
from models import QuestionModel, AnswerModel, CheckModel
from forms import QuestionForm
from Registration.views import check_validation
from forms import QuestionForm
# Create your views here.

def QuestionView(request):
    user = check_validation(request)
    if user:
        print user.count
        if user.count <= 20:
            question = QuestionModel.objects.order_by('?')[:1]
            while not CheckModel.objects.filter(question=question, user=user):
                user.count += 1
                user.save()
                served = CheckModel(question=question.first(), user=user)
                served.save()
                return render(request, 'index.html', {'question':question})
        else:
            return redirect('/endquiz/')
    else:
        return redirect('/login/')

def CheckAnswerView(request):
    user = check_validation(request)
    if user and request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            response = form.cleaned_data.get('answer')
            id = form.cleaned_data.get('question')
            answer = QuestionModel.objects.filter(id=id).answer
            if answer == response:
                pseudo = UserModel.objects.filter(id=user.id).first()
                pseudo.score = pseudo.score + 1
                pseudo.save()
                print pseudo
        return redirect('/quiz/')
    else:
        return redirect('/login/')
