from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

# Create your views here.

@login_required ##Login required to display the items selected
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {##below we will pass the items from here

        'items':items,


    } )










