from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
#        return self.order_by('-added_at')
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True, \
        related_name='question_to_author', on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_to_likes', blank=True)
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', args=(self.pk,))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text