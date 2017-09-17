from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
        request.session['comments'] = request.POST['comments']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'surveys/result.html')