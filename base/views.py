from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse
# We get rid of HttResponse after adding our template in Settings and use render
from .forms import RoomForm
# Create your views here.
# rooms = [
#     {'id': 1, 'name': "Let learn Python"},
#     {'id': 2, 'name': "Design with me"},
#     {'id': 3, 'name': "Back end developers"},
# ]

def loginPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=user_name)
        except:
            messages.error(request, 'User does not exist')
        
        user =  authenticate(request, username=user_name, password=user_password) 
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist.')
    context= {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # get used to get one single item from Room
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        # is the form is valid, form data into db and redirect the user to home page.
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
