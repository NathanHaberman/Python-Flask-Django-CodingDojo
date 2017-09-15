from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "All surveys"
    return HttpResponse(response)

def new(request):
    response = "Add new survey"
    return HttpResponse(response)