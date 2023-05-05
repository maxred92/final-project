from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from product.models import Things
from users.models import Profile

from .forms import MessageForm
from .models import Communication, Message
from .tasks import replace_text_with_censored


@login_required
def new_communication(request, things_pk):
    things = get_object_or_404(Things, pk=things_pk)
    profile = get_object_or_404(Profile, user=request.user)

    if things.created_by == request.user:
        return redirect('users:profile')
    
    communication = Communication.objects.filter(things=things).filter(members__in=[request.user.id])

    if communication:
        pass
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            communication = Communication.objects.create(things=things)
            communication.members.add(request.user)
            communication.members.add(things.created_by)
            communication.save()

            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user
            communication_message.save()
            replace_text_with_censored.delay(communication_message.id)

            return redirect('product:detail', pk=things_pk)

    else:
        form = MessageForm()

    return render(request, 'communication/new.html', {
        'form': form,
        'things': things,
        'profile': profile
    })

@login_required
def detail(request, pk):
    communication = Communication.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user
            communication_message.save()
            communication.save()
            replace_text_with_censored.delay(communication_message.id)

            return redirect('communication:detail', pk=pk)
    else:
        form = MessageForm()

    return render(request, 'communication/detail.html', {
        'communication': communication,
        'form': form
    })    

@login_required
def edit(request, pk):
    content = get_object_or_404(Message, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES, instance=content)

        if form.is_valid():
            content = form.save(commit=False)
            content.created_by = request.user
            content.save()
            replace_text_with_censored.delay(content.id)
            return redirect('communication:inbox')
    else:
        form = MessageForm(instance=content)
    context = {
        'form': form,
        'title': 'Edit message',}
    return render(request, 'communication/edit.html', context
    )

@login_required
def delete(request, pk):
    content = get_object_or_404(Message, pk=pk, created_by=request.user)
    content.delete()

    return redirect('communication:inbox')


@login_required
def inbox(request):
    communications = Communication.objects.filter(members__in=[request.user.id])

    return render(request, 'communication/inbox.html', {
        'communications': communications
    })