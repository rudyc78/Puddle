from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation
# Create your views here.


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard.index')

    conversation = Conversation.objects.filter(item=item).filter(members_in=[request.user.id])

    if conversation:
        pass # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)




