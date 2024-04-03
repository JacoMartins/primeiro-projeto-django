from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }

    return render(request, 'index.html', context)


def produto(request, pk):
    # produto = Produto.objects.get(pk=pk)
    produto = get_object_or_404(Produto, pk=pk)
    
    context = {
        'produto': produto
    }

    return render(request, 'produto.html', context)


def contato(request):
    return render(request, 'contato.html')


def error_404(request, exception):
    template = loader.get_template('404.html')

    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error_500(request):
    template = loader.get_template('500.html')

    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500) 