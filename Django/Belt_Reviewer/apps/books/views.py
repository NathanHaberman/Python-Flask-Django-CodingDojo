from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..login_and_registration.models import User
from models import Book, Review, Author
from ..login_and_registration.models import User

# Create your views here.
def home(request):
    user = User.objects.get(id = request.session['logged_in_user'])
    reviews = Review.objects.order_by('-created_at')[:3]
    books = Book.objects.all()

    context = {
        'name' : user.first_name,
        'reviews' : reviews,
        'books' : books,
    }

    return render(request, 'books/home.html', context)



def add(request):
    context = {
        "authors" : Author.objects.all()
    }

    return render(request, 'books/add.html', context)



def submit(request):
    if request.method == 'POST':
    
        # Checking if there are errors
        errors = Book.objects.valid(request.POST) + Author.objects.valid(request.POST) + Review.objects.valid(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/books/add/')


        # Add book and review to database
        else:
            title = request.POST['title']
            stars = request.POST['stars']
            reviewer = User.objects.get(id=request.session['logged_in_user'])

            # Checking if they entered a new author
            if len(request.POST['new_author']) > 0:

                # Adding new author to databae
                author = Author.objects.create(name=request.POST['new_author'])
                author.save()

            else:    
                author = Author.objects.get(name=request.POST['author'])

            # Adding new book to database
            book = Book.objects.create(title=title, author=author)
            book.save()

            # Adding new review to database
            Review.objects.create(content= review, stars=stars, reviewed_book=book, reviewer=reviewer)

            return redirect('/books/')

    else:
        return redirect('/books/add/')



def book_page(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(reviewed_book=book)

    context = {
        'book' : book,
        'reviews' : reviews,
    }

    return render(request, 'books/book_page.html', context)



def review(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        reviewer = User.objects.get(id=request.session['logged_in_user'])

        # Add new Review
        Review.objects.create(content=request.POST['review'], stars=request.POST['stars'], reviewed_book=book, reviewer=reviewer)

    return redirect('/books/' + str(book_id) + '/')

def delete(request, review_id):
    if request.method == 'POST':
        
        # Select the correct review to delete
        review_to_delete = Review.objects.get(id=int(review_id))
        review_to_delete.delete()

    return redirect('/books/')

def user_page(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id),
        'total_reviews' : Review.objects.filter(reviewer=user_id).count()
    }

    return render(request, 'books/user_page.html', context)