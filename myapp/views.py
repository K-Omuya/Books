from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookExchangeForm
from .models import BookExchange

from django.shortcuts import render
from .models import BookDonation


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookPledgeForm, BookDonationForm
from .models import BookPledge, BookDonation

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm




def exchange_book(request):
    return render(request, 'exchange_book.html')
def index(request):
    return render(request, 'index.html')


def about_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('about_contact')
    else:
        form = ContactForm()

    return render(request, 'about_contact.html', {'form': form})





def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_blog_post')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})

def view_blogs(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'view_blog_posts.html', {'blog_posts': blog_posts})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BookClub
from .forms import BookClubForm


def book_club_list(request):
    """View all book clubs"""
    clubs = BookClub.objects.all()
    return render(request, 'book_clubs.html', {'clubs': clubs})


def create_book_club(request):
    """Create a new book club"""
    if request.method == 'POST':
        form = BookClubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book club created successfully!")
            return redirect('view_book_clubs')
    else:
        form = BookClubForm()

    return render(request, 'create_book_club.html', {'form': form})



def pledge_book(request):
    if request.method == 'POST':
        form = BookPledgeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your pledge! We appreciate your support.")
            return redirect('pledge_book')
    else:
        form = BookPledgeForm()

    return render(request, 'pledge_book.html', {'form': form})


def donate_book(request):
    if request.method == 'POST':
        form = BookDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your book donation!")
            return redirect('donate_book')
    else:
        form = BookDonationForm()

    return render(request, 'donate_book.html', {'form': form})


def monetary_donation(request):
    return render(request, 'monetary_donation.html')





def book_list(request):
    query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')

    books = BookExchange.objects.all()

    if query:
        books = books.filter(book_title__icontains=query) | books.filter(author__icontains=query)

    if genre_filter:
        books = books.filter(genre=genre_filter)

    return render(request, 'view_books_catalogue.html', {'books': books})


def upload_book(request):
    if request.method == 'POST':
        form = BookExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.payment_status = False  # Assume payment is pending
            book.save()
            messages.success(request, "Your book has been listed! Please complete the payment of 20 KES.")
            return redirect('payment_page', book.id)
    else:
        form = BookExchangeForm()

    return render(request, 'upload_book.html', {'form': form})


def payment_page(request, book_id):
    book = BookExchange.objects.get(id=book_id)
    book.payment_status = True  # Simulate successful payment
    book.save()
    messages.success(request, "Payment successful! Your book is now listed for exchange.")
    return redirect('book_list')





def impacts(request):
    return render(request, 'impacts.html')

def view_blog_post(request):
    return render(request, 'view_blog_posts.html')

def view_book_clubs(request):
    return render(request, 'view_book_clubs.html')

def view_books_catalogue(request):
    return render(request, 'view_books_catalogue.html')




from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BookExchange, ContactMessage, BlogPost

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users_count = User.objects.count()
    books_count = BookExchange.objects.count()
    messages_count = ContactMessage.objects.count()
    blogs_count = BlogPost.objects.count()

    context = {
        'users_count': users_count,
        'books_count': books_count,
        'messages_count': messages_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'admin_dashboard.html', context)


def view_donated_books(request):
    donated_books = BookDonation.objects.all()

    # Translate book_type choices for display
    for book in donated_books:
        book.book_type_display = dict(BookDonation.BOOK_TYPES).get(book.book_type)
        book.delivery_option_display = dict(BookDonation.DELIVERY_OPTIONS).get(book.delivery_option)

    return render(request, 'view_donated_books.html', {'donated_books': donated_books})

# views.py
from django.shortcuts import render, redirect
from .models import BookDonation
from .forms import BookDonationForm

def book_exchange(request):
    # Retrieve all donated books
    donated_books = BookDonation.objects.all()

    # Handle the form submission
    if request.method == 'POST':
        form = BookDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_exchange')  # Redirect back to the book exchange page after submission
    else:
        form = BookDonationForm()

    return render(request, 'books_for_all.html', {'form': form, 'donated_books': donated_books})
