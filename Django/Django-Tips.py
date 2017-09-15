Creation
1) create a Django project
    --> django-admin startproject <project name goes here>


2) create an 'apps' folder
    --> cd <project name goes here>
    --> mkdir apps
    # --> cd <project name goes here>
    # --> md apps


3) create dunder-file in apps folder
    --> cd apps
    --> touch __init__.py

    # --> cd apps
    # --> copy nul __init__.py


4) create an app in the 'apps' folder
    --> python ../manage.py startapp <app name goes here>


5) create urls.py file inside of newly created app
    --> cd <app name goes here>
    --> touch urls.py
    # --> cd <app name goes here>
    # --> copy nul urls.py



Edit
1) settings.py in project folder-> register newly created app
    in INSTALLED_APPS:
    'apps.<appname>'
    'django_extensions'


2) include app urls.py in project urls.py
    url, include
    url(r'^', include('apps.<appname>.urls'), namespace='users')


3) create a method in app's views.py

      from django.shortcuts import render, HttpResponse

      def index(request):
        response = "Hello, I am your first request!"
        return HttpResponse(response)

        In a render file names / not .


4) update app's urls.py file with route
    from django.conf.urls import url
     from views import *
     urlpatterns = [
       url(r'^$', index, name = 'my_index'),
     ]

Check to see if everything is ok:
    run server:
    python manage.py runserver