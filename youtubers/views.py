from django.shortcuts import render
from django.http import HttpResponse
from .models import Youtuber


# Create your views here.
def youtubers(request):
    ytrs = Youtuber.objects.order_by('-created_date')
    data = {
        'ytrs': ytrs
    }
    return render(request, 'youtubers/youtuber.html', data)


def serach(request):
    return HttpResponse('search', render(request, 'youtubers/serach.html'))


def youtubers_detail(request, id):
    return render(request, 'youtubers/youtubers_detail.html')
