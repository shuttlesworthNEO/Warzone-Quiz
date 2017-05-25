# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Exam(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Question(models.Model):
	question_text = models.CharField(max_length=256)
	is_published = models.BooleanField(default=False)
	exam = models.ForeignKey(Exam, related_name='questions')

	def __str__(self):
		return "{content} - {published}".format(content=self.question_text, published=self.is_published)

class Answer(models.Model):
	text = models.CharField(max_length=128)
	is_valid = models.BooleanField(default=False)
	question = models.ForeignKey(Question, related_name='answers')

	def __str__(self):
		return self.text