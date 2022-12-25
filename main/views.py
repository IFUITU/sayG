from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from .models import Message, Room
from .serializer import MessageSerializer, RoomSeriazier
from .forms import MessageForm


# @login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': rooms})

# @login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

def lobby(request,pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room=room)[0:25]
    form  = MessageForm()
    if request.method == "post":
        form = MessageForm(request.POST)

    return render(request, 'chat/lobby.html', {"room": room , 'message': messages, 'form': form})


class RoomApiView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSeriazier
    permission_class = [IsAuthenticated]


class MessageApiView(ListCreateAPIView):
    queryest = Message.objects.all()
    serializer_class = MessageSerializer
    permission_class = [IsAuthenticated]


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSeriazier
    permission_classes = [IsAuthenticated]


class MessageByRoom(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        objs = Message.objects.filter(room_id=room_id)
        return objs

    




