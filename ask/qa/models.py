from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular():
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User, null=True, \
        related_name='question_to_author', on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_to_likes')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)