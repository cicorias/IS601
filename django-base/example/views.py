from django.http import (HttpResponse,
                         HttpRequest,
                         Http404,
                         HttpResponseRedirect)
from django.shortcuts import render
# from django.template import loader


from .models import BakedGood
from .forms import BakedGoodForm

# https://docs.djangoproject.com/en/3.0/topics/forms/
# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)

        if form.is_valid():
            #
            # use the ID or someting that created this and 302
            return HttpResponseRedirect('/')

    else:
        form = BakedGoodForm()

    return render(request, 'example/index.html', {'form': form})

    # baked_good_list = BakedGood.objects.all()  # ('name')
    # # output = ', '.join([i.name for i in baked_good_list])
    # # return HttpResponse(output)
    # context = {'baked_good_list': baked_good_list}
    # return render(request, 'example/index.html', context)


def detail(request: HttpRequest, item_id: int):
    try:
        item = BakedGood.objects.get(pk=item_id)
    except BakedGood.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'example/detail.html', {'item': item})
