from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("DEMO PAGE")


def hello(request):

    response_data = {}
    response_data['name'] = 'Victor Kean'
    response_data['age'] = 30

    return JsonResponse(response_data)
