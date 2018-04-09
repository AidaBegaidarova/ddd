from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from django.http import HttpResponse 

from qa.models import Question

@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def last_questions(request):
    query_set = Question.objects.new()
    return paginate(request, query_set, 'last_questions', 'sorted_questions.html')

@require_GET
def popular_questions(request):
    query_set = Question.objects.popular()
    return paginate(request, query_set, 'popular_questions', 'sorted_questions.html')

def paginate(request, query_set, reverse_url_name, template_name):
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try: 
        limit = int(request.GET.get('limit', 1))
    except:
        limit = 1
    if limit > 1:
        limit = 1
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

@require_GET
def question_detials(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'question.html', {
        'question': question
    })