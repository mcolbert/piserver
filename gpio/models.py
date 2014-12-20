from django.db import models

# Create your models here.

class QuestionTest(models.Model):
  question_text = models.CharField(max_length=200)
