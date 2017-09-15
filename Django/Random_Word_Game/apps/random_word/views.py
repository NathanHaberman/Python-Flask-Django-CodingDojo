from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'random_word/index.html')

def reset(request):
    if request.method == "POST":
        for key in request.session.keys():
            del request.session[key]
        return redirect('/')
    else:
        return redirect('/')

def generate(request):
    if request.method == "POST":
        request.session['count'] += 1
        request.session['word_generated'] = get_random_string(12)
        return redirect('/')
    else:
        return redirect('/')