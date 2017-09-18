from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'total' in request.session:
        request.session['total'] = 0
    return render(request, 'amadon/index.html')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def buy(request):
    if request.method == 'POST':
        items = {
            '1' : 19.99,
            '2' : 9.99,
            '3' : 29.99
        }

        item_id = str(request.POST['item_id'])
        amount = float(request.POST['amount'])

        request.session['total'] += float(items[item_id]) * amount
        return redirect('checkout/')
    else:
        return redirect('/')

def reset(request):
    if request.method == "POST":
        return redirect('/')
    else:
        return redirect('/')