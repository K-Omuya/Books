from django.urls import path
from . import views

from django.urls import path
from .views import book_club_list, create_book_club

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('about_contact/', views.about_contact, name='about_contact'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('create_book_club/', views.create_book_club, name='create_book_club'),
    path('donate_book/', views.donate_book, name='donate_book'),

    path('impacts/', views.impacts, name='impacts'),
    path('view_blog_post/', views.view_blog_post, name='view_blog_post'),
    path('exchange_book/', views.exchange_book, name='exchange_book'),
    path('view_book_clubs/', views.view_book_clubs, name='view_book_clubs'),
    path('view_books_catalogue/', views.view_books_catalogue, name='view_books_catalogue'),
    path('view_donated_books/', views.view_donated_books, name='view_donated_books'),




    path('book-clubs/', views.book_club_list, name='book_club_list'),
    path('book-clubs/create/', views.create_book_club, name='create_book_club'),

    path('pledge/', views.pledge_book, name='pledge_book'),
    path('donate/', views.donate_book, name='donate_book'),
    path('monetary/', views.monetary_donation, name='monetary_donation'),

    path('books/', views.book_list, name='book_list'),
    path('upload/', views.upload_book, name='upload_book'),
    path('payment/<int:book_id>/', views.payment_page, name='payment_page'),



    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),



]
