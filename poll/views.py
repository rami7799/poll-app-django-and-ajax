from django.http import JsonResponse
from django.shortcuts import render
from .models import Poll
from question.models import Question , Answer

def home(request):
    poll = Poll.objects.all()   
    return render(request , "home.html" , {"poll" : poll})

def poll(request , pk):
    poll = Poll.objects.get(pk=pk)
    return render(request , "poll.html" , {"poll" : poll})


def get_data(request , pk):
    id = request.GET.get("id")
    print(id)
    answer = Answer.objects.get(pk=id)
    answer.score += 1
    answer.save()
    return JsonResponse({"data" : "successed"})