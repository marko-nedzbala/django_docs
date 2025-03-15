from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    # return HttpResponse('Hellow, world, you are at the polls index')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
    response = f'You are looking at the results of question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')


