from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'users/index.html', context)

def user(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'users/user.html', context)

def new(request):
    return render(request, 'users/new_user.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.valid(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/users/new')
        else:
            User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
            return redirect('/users')
    else:
        return redirect('/users/new')


def edit(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'users/edit_user.html', context)

def update(request, user_id):
    if request.method == 'POST':
        errors = User.objects.valid(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/users/edit')
        else:
            user_updated = User.objects.get(id=user_id)
            user_updated.first_name = request.POST['first_name']
            user_updated.last_name = request.POST['last_name']
            user_updated.email = request.POST['email']
            user_updated.save()
            return redirect('/users')

def destroy(request, user_id):
    if request.method == 'POST':
        user_delete = User.objects.get(id=user_id)
        user_delete.delete()
    return redirect('/users')