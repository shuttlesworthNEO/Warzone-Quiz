# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Quiz.models import Exam, Question, Answer

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)