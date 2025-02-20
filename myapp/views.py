from .forms import ContactForm
import json
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import BlogPost
from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword




def landing(request):
    return render(request, 'landing.html')

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


def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def user_profile(request):
    return render(request, 'profile.html')
def blog_detail(request):
    return render(request, 'blog_list.html')

def book_club_list(request):
    """View all book clubs"""
    clubs = BookClub.objects.all()
    return render(request, 'view_book_clubs.html', {'clubs': clubs})

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

def view_book_clubs(request):
    return render(request, 'view_book_clubs.html')


def is_admin(user):
    return user.is_superuser

def view_donated_books(request):
    donated_books = BookDonation.objects.all()

    # Translate book_type choices for display
    for book in donated_books:
        book.book_type_display = dict(BookDonation.BOOK_TYPES).get(book.book_type)
        book.delivery_option_display = dict(BookDonation.DELIVERY_OPTIONS).get(book.delivery_option)

    return render(request, 'view_donated_books.html', {'donated_books': donated_books})



def token(request):
        consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
        consumer_secret = 'viM8ejHgtEmtPTHd'
        api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))
        mpesa_access_token = json.loads(r.text)
        validated_mpesa_access_token = mpesa_access_token["access_token"]

        return render(request, 'pay.html', {"token": validated_mpesa_access_token})

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


from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to blog list after creating
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', {'form': form})



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


def index(request):
    impact, created = ImpactData.objects.get_or_create(id=1)  # Ensure a default record exists

    context = {
        "students_impacted": impact.students_impacted,
        "schools_reached": impact.schools_reached,
        "book_exchanges": impact.book_exchanges,
        "books_donated": impact.books_donated,
    }
    return render(request, 'index.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from .models import ImpactData
from .forms import ImpactDataForm

def edit_impact(request):
    impact_data = ImpactData.objects.first()  # Get the first impact data entry
    if not impact_data:
        impact_data = ImpactData.objects.create()  # Create default entry if none exists

    if request.method == "POST":
        form = ImpactDataForm(request.POST, instance=impact_data)
        if form.is_valid():
            form.save()
            return redirect('edit_impact')  # Refresh the page after saving

    else:
        form = ImpactDataForm(instance=impact_data)

    return render(request, 'edit_impact.html', {'form': form})



from django.contrib import admin
from django.template.response import TemplateResponse

class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    index_template = "admin/custom_index.html"

    def index(self, request, extra_context=None):
        return TemplateResponse(request, self.index_template, extra_context)

admin_site = CustomAdminSite(name='custom_admin')



