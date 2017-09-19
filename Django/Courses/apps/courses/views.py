from django.shortcuts import render, redirect
from django.contrib import messages
from models import Course

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == "POST":
        errors = Course.objects.valid(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/courses')
        else:
            Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
            return redirect('/courses')

def check(request, course_id):
    context = {
        'course' : Course.objects.get(id=course_id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, course_id):
    if request.method == 'POST':
        trash = Course.objects.get(id=course_id)
        trash.delete()
        return redirect('/courses')
    else:
        return redirect('/courses')