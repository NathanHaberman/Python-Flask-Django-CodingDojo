from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

import bcrypt


# Create your views here.
def index(request):
    return render(request, 'login_and_registration/index.html')



def register(request):
    if request.method == 'POST':
        
        # Checking if there are errors from models
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        
        else:
            # Encrypting Password
            password = request.POST['password']
            password = password.encode('utf8')
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            # Adding user
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            
            # Logging in person
            user = User.objects.get(email = request.POST['email'])
            request.session['logged_in_user'] = user.id
            
            return redirect('/books/')
    else:
        return redirect('/')



def login(request):
    # Checking if there is a matching email
    user_in_db = User.objects.filter(email = request.POST['email'])
    
    if user_in_db:
        
        # Now checking if password matched the encrypted one in the database
        if bcrypt.checkpw(request.POST['password'].encode('utf8'), user_in_db[0].password.encode('utf8')):
            request.session['logged_in_user'] = user_in_db[0].id
            
            return redirect('/books/')
        
        else:
            # Error if passwords don't match
            messages.error(request, 'Password is incorrect')
            return redirect('/')
    
    else:
        # If email is not in database
        messages.error(request, 'Email is incorrect')
        return redirect('/')



def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')



def user_page(request, user_id):
    pass