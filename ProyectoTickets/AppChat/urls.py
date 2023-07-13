from django.urls import path
from AppChat.views import *

urlpatterns = [
  path('chat_room/', chat_room, name="chat_room"),
]