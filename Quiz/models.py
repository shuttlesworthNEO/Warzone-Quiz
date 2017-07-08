# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from Registration.models import UserModel

# Create your models here.
@python_2_unicode_compatible
class QuestionModel(models.Model):
	question_text = models.CharField(max_length=2000)
	option1 = models.CharField(max_length=240)
	option2 = models.CharField(max_length=240)
	option3 = models.CharField(max_length=240)
	option4 = models.CharField(max_length=240)
	url = models.CharField(max_length=240, default=None, blank=True)
	answer = models.CharField(max_length=5)
	def __str__(self):
		return self.question_text

class CheckModel(models.Model):
	question = models.ForeignKey(QuestionModel)
	user = models.ForeignKey(UserModel)
	served = models.BooleanField(default=True)

class AnswerModel(models.Model):
	question = models.ForeignKey(QuestionModel)