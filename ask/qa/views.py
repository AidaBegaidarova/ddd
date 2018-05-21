from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .models import Question
from .forms import AskForm, AnswerForm, SignupForm, LoginForm

@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
@login_required
def last_questions(request):
    query_set = Question.objects.new()
    return paginate(request, query_set, 'new', 'sorted_questions.html')

@require_GET
@login_required
def popular_questions(request):
    query_set = Question.objects.popular()
    return paginate(request, query_set, 'popular', 'sorted_questions.html')

def paginate(request, query_set, reverse_url_name, template_name):
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try: 
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    if limit > 10:
        limit = 10
    paginator = Paginator(query_set, limit)
    paginator.baseurl = reverse(reverse_url_name)+'?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, template_name, {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page 
    })

@login_required
def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question_detail.html', {
        'question': question, 'form': form
    })

@login_required
def question_ask(request):
    if request.method == 'POST':
        form = AskForm(data=request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_ask.html', {
        'form': form
        })
    
def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(user)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {
        'form': form
        })

def login_user(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Invalid login or password!'
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {
        'form': form, 
        'error': error
        })