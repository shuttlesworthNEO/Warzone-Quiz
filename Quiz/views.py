# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import QuestionModel
from forms import QuestionForm

# Create your views here.

def quiz_view(request):
