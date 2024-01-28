from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # the code below uses try except pattern
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    #  the code below uses django's shortcut for error 404 handling, this is shorter
    #  so we will be using this

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
