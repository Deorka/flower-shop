from django.shortcuts import render, get_object_or_404
from django.db.models import Min
from .models import Flower, Item, Genus, Species
from django.db.models import Q
from django.views.generic import TemplateView, ListView


def main_page(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/main_page.html', {'genuses': genuses})


def catalog(request):
    flowers = Flower.objects.all()
    # Сортировка
    order = request.GET.get('order')
    if order:
        if order == 'items__price':
            flowers = flowers.annotate(min_price=Min('items__price')).order_by('min_price')
            #flowers = flowers.annotate(available=Min('item__available')).order_by('available')
        else:
            flowers = flowers.order_by(order)
    # Род
    genuses = Genus.objects.all()
    genus_name = request.GET.get('genus')
    if genus_name:
        flowers = flowers.filter(species__genus__name=genus_name)
    # Вид
    specieses = Species.objects.all()
    specieses_name = request.GET.get('species')
    if specieses_name:
        flowers = flowers.filter(species__name=specieses_name)

    # Высота
    heightl = request.GET.get('heightl')
    heightr = request.GET.get('heightr')
    if heightl:
        flowers = flowers.filter(height__gte=heightl)
    if heightr:
        flowers = flowers.filter(height__lte=heightr)

    return render(request, 'shop/catalog.html', {'flowers': flowers, 'genuses': genuses, 'specieses': specieses})


def index(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/index.html', {'genuses': genuses})


def delivery_pay(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/delivery_pay.html', {'genuses': genuses})


def exchange_return(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/exchange_return.html', {'genuses': genuses})


def info(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/info.html', {'genuses': genuses})


def contacts(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/contacts.html', {'genuses': genuses})


def flower_item(request, pk):
    genuses = Genus.objects.all()
    flower = get_object_or_404(Flower, pk=pk)
    return render(request, 'shop/flower_item.html', {'flower': flower, 'genuses': genuses})


def we(request):
    genuses = Genus.objects.all()
    return render(request, 'shop/we.html', {'genuses': genuses})


def example(request, pk):
    genuses = Genus.objects.all()
    flower = get_object_or_404(Flower, pk=pk)
    return render(request, 'shop/example.html', {'flower': flower, 'genuses': genuses})
