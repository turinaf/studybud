from django.shortcuts import render
from .models import Room
# from django.http import HttpResponse
# We get rid of HttResponse after adding our template in Settings and use render

# Create your views here.
# rooms = [
#     {'id': 1, 'name': "Let learn Python"},
#     {'id': 2, 'name': "Design with me"},
#     {'id': 3, 'name': "Back end developers"},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # get used to get one single item from Room
    context = {'room': room}
    return render(request, 'base/room.html', context)