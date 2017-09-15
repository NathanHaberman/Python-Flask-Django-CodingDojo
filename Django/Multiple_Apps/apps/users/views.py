from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register(request):
    response = "Registration form"
    return HttpResponse(response)

def login(request):
    response = "Login"
    return HttpResponse(response)

def users(request):
    response = "List of users"
    return HttpResponse(response)