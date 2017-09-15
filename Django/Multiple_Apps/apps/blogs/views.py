from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "List of blogs"
    return HttpResponse(response)

def new_blog(request):
    response = "New Blog Form"
    return HttpResponse(response)

def create_blog(request):
    return redirect('/')

def blog(request, number):
    print "Made it"
    response = "Blog Number: " + str(number)
    return HttpResponse(response)