from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.template import loader


# from .models import BakedGood
def index(request):
    return JsonResponse({ 'foo': 'bar'})
    # return HttpResponse('foobar',  )