
from django.contrib.auth.decorators import login_required
from django.db.models import Q ##This will look for the description from the database
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

# Create your views here.

def items(request):
    query = request.GET.get('query','')##This will make the search bar available
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query)) ##the query will processed, backend for search bar





    return render(request, 'item/items.html', {
    'items': items,
    'query': query,
    'categories': categories,
    'category_id':int(category_id),

    })

def detail(request, pk): ##pk is for primary key
    item = get_object_or_404(Item, pk=pk) ##first pk is from the model itself and second from the url
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'item/detail.html',{

        'item':item,
        'related_items': related_items,

    } )

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)


        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:

        form = NewItemForm()

    return render(request, 'item/form.html',{

        
        'form':form,
        'title':'New item',

    })
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)


        if form.is_valid():
            
            form.save()

            return redirect('item:detail', pk=item.id)
    else:

        form = EditItemForm(instance=item)##This is in order to pass the items when editing the form

    return render(request, 'item/form.html',{

        
        'form':form,
        'title':'Edit item',

    })
@login_required ##This is required, since we need to be logged in to delete items
def delete(request, pk): ##pk the id of the item we want to remove
    item = get_object_or_404(Item, pk=pk, created_by=request.user)##We select the items retrived from the database.
    item.delete()


    return redirect('dashboard:index')




