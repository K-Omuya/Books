from .forms import ContactForm
import json
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse
from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword


def landing(request):
    return render(request, 'landing.html')
def index(request):
    return render(request, 'index.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


from django.contrib.auth import authenticate, login

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Check if any field is empty
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('register')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')




def landing(request):
    return render(request, 'landing.html')



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








def view_blog_post(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'view_blog_post.html', {'blog_posts': blog_posts})


from django.shortcuts import render

def user_profile(request):
    return render(request, 'profile.html')  # Make sure to create the profile.html template


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BookClub
from .forms import BookClubForm


def book_club_list(request):
    """View all book clubs"""
    clubs = BookClub.objects.all()
    return render(request, 'view_book_clubs.html', {'clubs': clubs})


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
            return redirect('pay', book.id)
    else:
        form = BookExchangeForm()

    return render(request, 'upload_book_form.html', {'form': form})




def impacts(request):
    return render(request, 'impacts.html')


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












def token(request):
        consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
        consumer_secret = 'viM8ejHgtEmtPTHd'
        api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))
        mpesa_access_token = json.loads(r.text)
        validated_mpesa_access_token = mpesa_access_token["access_token"]

        return render(request, 'token.html', {"token": validated_mpesa_access_token})

def pay(request):
        return render(request, 'pay.html')

def stk(request):
        if request.method == "POST":
            phone = request.POST['phone']
            amount = request.POST['amount']
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone,
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": phone,
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "SIMON OTIENO",
                "TransactionDesc": "Web Development Charges"
            }
            response = requests.post(api_url, json=request, headers=headers)
            return HttpResponse("Request sent successfully check your phone to input pin")


from django.shortcuts import render, redirect
from .models import BookClub
from .forms import BookClubForm


def book_clubs_list(request):
    clubs_by_county = {}
    for club in BookClub.objects.all():
        if club.county not in clubs_by_county:
            clubs_by_county[club.county] = []
        clubs_by_county[club.county].append(club)

    return render(request, 'book_clubs_list.html', {'clubs_by_county': clubs_by_county})


def add_book_club(request):
    if request.method == 'POST':
        form = BookClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_clubs_list')
    else:
        form = BookClubForm()
    return render(request, 'add_book_club.html', {'form': form})






from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to blog list after creating
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', {'form': form})


from django.shortcuts import render, redirect
from .models import BookDonation
from .forms import BookDonationForm



from django.shortcuts import render, redirect
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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BookExchange
from .forms import BookExchangeForm


def book_exchange_list(request):
    query = request.GET.get('q')
    books = BookExchange.objects.all()

    if query:
        books = books.filter(title__icontains=query)  # Search by title

    return render(request, 'book_exchange_list.html', {'books': books})


def upload_book(request):
    if request.method == 'POST':
        form = BookExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book uploaded successfully!")
            return redirect('book_exchange_list')
    else:
        form = BookExchangeForm()

    return render(request, 'upload_book.html', {'form': form})

from django.shortcuts import render
from .models import Book

def exchanged_books(request):
    exchanged = Book.objects.filter(exchanged=True)  # Assuming an "exchanged" field exists
    return render(request, 'exchanged_books.html', {'books': exchanged})

from django.shortcuts import render, get_object_or_404, redirect


def exchange_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Check if the book exists
    return render(request, 'exchange_book.html', {'book': book})  # Redirect to payment

def book_payment(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.exchanged = True  # Mark book as exchanged
        book.save()
        messages.success(request, f'Payment successful! {book.title} is now awaiting delivery.')
        return redirect('exchanged_books')  # Redirect to exchanged books page

    return render(request, 'payment.html', {'book': book})
