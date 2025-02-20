from django.contrib.auth.views import LoginView
from . import views
from django.urls import path



urlpatterns = [
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('login/',  views.user_login, name='login'),
    path('register/',  views.user_register, name='register'),
    path('accounts/profile/', views.user_profile, name='profile'),
    path('about_contact/', views.about_contact, name='about_contact'),
    path('donate_book/', views.donate_book, name='donate_book'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('view_book_clubs/', views.view_book_clubs, name='view_book_clubs'),
    path('view_donated_books/', views.view_donated_books, name='view_donated_books'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('upload/', views.upload_book, name='upload_book'),
    path('exchange/', views.book_exchange_list, name='book_exchange_list'),
    path('exchange/upload/', views.upload_book, name='upload_book'),
    path('edit_impact/', views.edit_impact, name='edit_impact'),
    path('exchange/', views.book_exchange_list, name='book_exchange_list'),
    path('upload/', views.upload_book, name='upload_book'),
    path('book-clubs/', views.book_club_list, name='book_club_list'),
    path('pledge/', views.pledge_book, name='pledge_book'),
    path('donate/', views.donate_book, name='donate_book'),
    path('upload/', views.upload_book, name='upload_book'),
    path('book_clubs_list/', views.book_clubs_list, name='book_clubs_list'),
    path('add/', views.add_book_club, name='add_book_club'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/new/', views.blog_create, name='blog_create'),
    path('donate/', views.donate_book, name='donate_book'),
    path('donated-books/', views.view_donated_books, name='view_donated_books'),
    path('pledge/', views.pledge_book, name='pledge_book'),
    path('pledged-books/', views.view_pledged_books, name='view_pledged_books'),
    path('pledge/', views.pledge_book, name='pledge_book'),
    path('view-pledges/', views.view_pledged_books, name='view_pledged_books'),





]