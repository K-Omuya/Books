from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'course.html')

def blogs(request):
    return render(request, 'blog.html')

def features(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def monetary_donations(request):
    return render(request, 'monetary_donations.html')
def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'blogs': blogs})

from django.shortcuts import render, redirect
from .models import Book, Pledge, BookClub
from .forms import BookForm, PledgeForm, BookClubForm

def donate_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_catalogue')
    else:
        form = BookForm()
    return render(request, 'donate_book.html', {'form': form})

def upload_book(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PledgeForm()
    return render(request, 'upload_book_exchange.html', {'form': form})


from .models import BookClub
from .forms import BookClubForm


def view_book_clubs(request):
    clubs_by_county = {}
    for club in BookClub.objects.all():
        if club.county not in clubs_by_county:
            clubs_by_county[club.county] = []
        clubs_by_county[club.county].append(club)

    return render(request, 'view_book_clubs.html', {'clubs_by_county': clubs_by_county})


def create_book_club(request):
    if request.method == 'POST':
        form = BookClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_book_clubs')
    else:
        form = BookClubForm()
    return render(request, 'create_book_club.html', {'form': form})





def book_catalogue(request):
    books = Book.objects.all()
    return render(request, 'book_exchange_catalogue.html', {'books': books})




from django.shortcuts import render, redirect
from .models import PledgedBook
from .forms import PledgedBookForm

def pledge_book(request):
    if request.method == 'POST':
        form = PledgedBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pledged_books')  # Redirect to pledged books list
    else:
        form = PledgedBookForm()
    return render(request, 'pledge_book.html', {'form': form})

def view_pledged_books(request):
    pledged_books = PledgedBook.objects.all().order_by('-pledge_date')  # Latest pledges first
    return render(request, 'view_pledged_books.html', {'pledged_books': pledged_books})

from .models import BookDonation
from .forms import BookDonationForm

def donate_book(request):
    if request.method == 'POST':
        form = BookDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_donated_books')
    else:
        form = BookDonationForm()
    return render(request, 'donate_book.html', {'form': form})

def view_donated_books(request):
    books = BookDonation.objects.all().order_by('-donated_at')
    return render(request, 'view_donated_books.html', {'books': books})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookExchangeForm
from .models import BookExchange


def upload_book_exchange(request):
    if request.method == "POST":
        form = BookExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            # Simulating payment confirmation for listing
            book.is_paid = True
            book.save()
            messages.success(request, "Payment successful! Your book has been uploaded.")
            return redirect('book_exchange_catalogue')
    else:
        form = BookExchangeForm()

    return render(request, 'upload_book_exchange.html', {'form': form})


def book_exchange_catalogue(request):
    genre_filter = request.GET.get('genre', '')
    books = BookExchange.objects.filter(is_paid=True)

    if genre_filter:
        books = books.filter(genre=genre_filter)

    return render(request, 'book_exchange_catalogue.html', {'books': books, 'genre_filter': genre_filter})

def pay_delivery(request, book_id):
    book = BookExchange.objects.get(id=book_id)
    book.delivery_paid = True
    book.save()
    messages.success(request, "Delivery payment of Ksh. 200 completed!")
    return redirect('book_exchange_catalogue')
