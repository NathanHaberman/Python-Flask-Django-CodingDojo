from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'log' in request.session:
        request.session['log'] = []
    return render(request, 'ninja_gold/index.html')

def gold(request):
    if request.method == "POST":
        buildings = {
            'farm' : random.randint(10,20),
            'cave' : random.randint(5,10),
            'house' : random.randint(2,5),
            'casino' : random.randint(0,50),
        }
        building = request.POST['building']
        request.session['past_gold'] = request.session['gold']

        if building == 'casino':
            chance = random.randint(1,4)
            if chance > 1:
                if request.session['gold'] < buildings[building]:
                    request.session['gold'] = 0
                    request.session['log'].append("You lost all your gold at the casino")
                    text_class = 'text-danger'
                else:
                    request.session['gold'] -= buildings[building]
                    request.session['log'].append("You lost " + str(buildings[building]) + " gold at the casino")
                    text_class = 'text-danger'
            else:
                request.session['gold'] += buildings[building]
                request.session['log'].append("You won " + str(buildings[building]) + " gold at the casino")
                text_class = 'text-success'
        else:
            request.session['gold'] += buildings[building]
            request.session['log'].append("You earned " + str(buildings[building]) + " gold at the " + str(building))
            text_class = 'text-success'
        return redirect('/', {'class' : text_class})
    else:
        return redirect('/')

def reset(request):
    if request.method == "POST":
        for key in request.session.keys():
            del request.session[key]
        return redirect('/')
    else:
        return redirect('/')