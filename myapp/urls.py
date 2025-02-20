from django.contrib.auth.views import LoginView
from django.urls import path
from . import views





from django.urls import path
from .views import book_club_list, create_book_club
from django.urls import path
from .views import admin_dashboard
from .views import admin_dashboard


from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('login/',  views.user_login, name='login'),
    path('register/',  views.user_register, name='register'),

    path('accounts/profile/', views.user_profile, name='profile'),
    path('about_contact/', views.about_contact, name='about_contact'),
    path('create_book_club/', views.create_book_club, name='create_book_club'),
    path('donate_book/', views.donate_book, name='donate_book'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('impacts/', views.impacts, name='impacts'),
    path('view_blog_post/', views.view_blog_post, name='view_blog_post'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('exchange_book/', views.exchanged_books, name='exchange_book'),
    path('view_book_clubs/', views.view_book_clubs, name='view_book_clubs'),
    path('view_books_catalogue/', views.view_books_catalogue, name='view_books_catalogue'),
    path('view_donated_books/', views.view_donated_books, name='view_donated_books'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('upload/', views.upload_book, name='upload_book'),
    path('exchange/', views.book_exchange_list, name='book_exchange_list'),
    path('exchange/upload/', views.upload_book, name='upload_book'),


    path('exchange/', views.book_exchange_list, name='book_exchange_list'),
    path('upload/', views.upload_book, name='upload_book'),


    path('payment/<int:book_id>/', views.book_payment, name='book_payment'),
    path('exchange/<int:book_id>/', views.exchange_book, name='exchange_book'),





    path('book-clubs/', views.book_club_list, name='book_club_list'),
    path('book-clubs/create/', views.create_book_club, name='create_book_club'),

    path('pledge/', views.pledge_book, name='pledge_book'),
    path('donate/', views.donate_book, name='donate_book'),
    path('monetary/', views.monetary_donation, name='monetary_donation'),

    path('books/', views.book_list, name='book_list'),
    path('upload/', views.upload_book, name='upload_book'),
    path('blog/<int:post_id>/', views.view_blog_post, name='view_blog_post'),  # Ensure this matches what you're reversing
    path('view_blog_post/<int:post_id>/', views.view_blog_post, name='view_blog_post'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('view_blog_post/', views.view_blog_post, name='view_blog_post'),




    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),



    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('book_clubs_list/', views.book_clubs_list, name='book_clubs_list'),
    path('add/', views.add_book_club, name='add_book_club'),
    path('blogs/', views.blog_list, name='blog_list'),

    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),  # Make sure <int:pk> is used
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/new/', views.blog_create, name='blog_create'),
    path('donate/', views.donate_book, name='donate_book'),
    path('donated-books/', views.view_donated_books, name='view_donated_books'),
    path('pledge/', views.pledge_book, name='pledge_book'),
    path('pledged-books/', views.view_pledged_books, name='view_pledged_books'),
    path('pledge/', views.pledge_book, name='pledge_book'),
    path('view-pledges/', views.view_pledged_books, name='view_pledged_books'),



]