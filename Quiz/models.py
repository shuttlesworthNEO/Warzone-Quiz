# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class QuestionModel(models.Model):
	question_text = models.CharField(max_length=2000)
	option1 = models.CharField(max_length=240)
	option2 = models.CharField(max_length=240)
	option3 = models.CharField(max_length=240)
	option4 = models.CharField(max_length=240)
	def __str__(self):
		return self.question_text