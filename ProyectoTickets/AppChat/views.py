from django.shortcuts import render, redirect
from AppChat.models import Mensaje
from AppChat.forms import CommentForm
from AppTickets.views import getavatar
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chat_room(request):
    mensajes = Mensaje.objects.order_by('-timestamp')
    avatar = getavatar(request)
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            mensaje=form.save(commit=False)
            mensaje.autorMensaje=request.user.username
            mensaje.save()

        return redirect('chat_room')
    return render(request, "AppChat/chat_room.html",{"mensajes":mensajes,"form":form,"avatar":avatar})



