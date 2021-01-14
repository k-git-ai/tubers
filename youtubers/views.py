from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def youtubers(request):
    return HttpResponse('youtubers', render(request, 'youtubers/youtuber.html'))


def serach(request):
    return HttpResponse('search', render(request, 'youtubers/serach.html'))


def youtubers_detail(request):
    return HttpResponse('youtubers_detail', render(request, 'youtubers/youtubers_detail.html'))
