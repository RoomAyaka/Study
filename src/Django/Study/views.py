from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def page(request, page_id):
    msg = f'ページ{page_id}'
    return HttpResponse(msg)


def index(request):
    template = loader.get_template('index.html')
    context = {
        "title": "Django",
        'message': 'index.htmlの表示'
    }
    return HttpResponse(template.render(context, request))
