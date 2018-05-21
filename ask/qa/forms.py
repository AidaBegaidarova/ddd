from django.contrib.auth.models import User
from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, **kwargs):
        super(AskForm, self).__init__(**kwargs)

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self,  **kwargs):
        super(AnswerForm, self).__init__(**kwargs)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['author'] = self._user
        return Answer.objects.create(**self.cleaned_data)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, **kwargs):
        super(SignupForm, self).__init__(**kwargs)

    def clean(self):
        pass

    def save(self):
        return User.objects.create_user(**self.cleaned_data)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, **kwargs):
        super(LoginForm, self).__init__(**kwargs)

    def clean(self):
        pass

    def save(self):
        pass