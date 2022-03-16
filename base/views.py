from django.shortcuts import render
# from django.http import HttpResponse
# We get rid of HttResponse after adding our template in Settings and use render

# Create your views here.
rooms = [
    {'id': 1, 'name': "Let learn Python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Back end developers"},
]

def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] ==  int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)