from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader


from .models import BakedGood


def index(request):
    baked_good_list = BakedGood.objects.all()  # ('name')
    # output = ', '.join([i.name for i in baked_good_list])
    # return HttpResponse(output)
    context = {'baked_good_list': baked_good_list}
    return render(request, 'example/index.html', context)


def detail(request, item_id):
    try:
        item = BakedGood.objects.get(pk=item_id)
    except BakedGood.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'example/detail.html', {'item': item})
