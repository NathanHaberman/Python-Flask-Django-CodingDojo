from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'words' in request.session:
        request.session['words'] = []
    return render(request, 'session_words/index.html')

def session_add(request):
    if request.method == "POST":
        new_word = {
            'word' : request.POST['new_word'],
            'color' : request.POST['color'],
            'size' : request.POST['size']
        }

        request.session['words'].append(new_word)
        print request.session.words
        return redirect('/')
    else:
        return redirect('/')