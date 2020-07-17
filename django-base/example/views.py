from django.http import (HttpResponse,
                         HttpRequest,
                         Http404,
                         HttpResponseRedirect,
                         JsonResponse)

from django.shortcuts import render
from django.urls import reverse
# from django.template import loader
from .models import BakedGood, BakedGoodForm, IngredientForm


def index(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_good_list': baked_goods}
    return render(request, 'example/index.html', context)


def bake(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)

        if form.is_valid():
            instance = form.save()
            # use the ID or someting that created this and 302
            return HttpResponseRedirect(
                reverse('bake-detail', args=[instance.id]))
            # return HttpResponseRedirect(reverse('bake-index'))
    else:
        form = BakedGoodForm()

    return render(request, 'example/bake.html', {'form': form})


def ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = IngredientForm()

    return render(request, 'example/ingredient.html', {'form': form})


def detail(request: HttpRequest, item_id: int):
    try:
        item = BakedGood.objects.get(pk=item_id)
        is_bread = True if item.good_type == 'BA' else False
    except BakedGood.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'example/detail.html',
                  {'item': item, 'isBread': is_bread})


def bakeapi(request: HttpRequest):
    '''the view that hosts the jquery calls'''
    items = BakedGood.objects.all()
    return render(request, 'example/bakeapi.html', {'items': items})


def bakeapidetail(request: HttpRequest, item_id: int):
    '''this is the json api endpoint called'''
    try:
        item = BakedGood.objects.get(pk=item_id).as_dict()
    except BakedGood.DoesNotExist:
        raise Http404("Question does not exist")

    return JsonResponse(item)
