from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def detail(request, pk): ##pk is for primary key
    item = get_object_or_404(Item, pk=pk) ##first pk is from the model itself and second from the url
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'item/detail.html',{

        'item':item,
        'related_items': related_items,

    } )




