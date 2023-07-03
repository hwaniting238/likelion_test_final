from django.shortcuts import render, redirect, get_object_or_404
from .models import Newapp
from django.utils import timezone

# Create your views here.

def home(request):
    newapps = Newapp.objects.all()
    return render(request, 'home.html', {'newapps':newapps})

def detail(request,id):
    newapp = get_object_or_404(Newapp, pk = id)
    return render(request, 'detail.html', {'newapp':newapp})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_newapp = Newapp()
    new_newapp.title = request.POST['title']
    new_newapp.intro = request.POST['intro']
    new_newapp.head = request.POST['head']
    new_newapp.save()
    return redirect('detail', new_newapp.id)

def edit(request,id):
    edit_newapp = Newapp.objects.get(id = id)
    return render(request, 'edit.html', {'newapp':edit_newapp})

def update(request, id):
    update_newapp = Newapp.objects.get(id = id)
    update_newapp.title = request.POST['title']
    update_newapp.intro = request.POST['intro']
    update_newapp.head = request.POST['head']
    update_newapp.save()
    return redirect('detail', update_newapp.id)

def delete(request, id):    
    delete_newapp = Newapp.objects.get(id=id)
    delete_newapp.delete()
    return redirect('home')


