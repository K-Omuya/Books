from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    book_type = models.CharField(
        max_length=50,
        choices=[('curriculum', 'Curriculum'), ('storybook', 'Storybook'), ('general', 'General Reading')]
    )
    drop_off_location = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Pledge(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    book_count = models.PositiveIntegerField()
    pledged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book_count} books"

from django.db import models

class BookClub(models.Model):
    school_name = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    students_count = models.IntegerField()
    patron_name = models.CharField(max_length=255)
    patron_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.school_name



class PledgedBook(models.Model):
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    book_title = models.CharField(max_length=255)
    book_type_choices = [
        ('curriculum', 'Curriculum'),
        ('storybook', 'Storybook'),
        ('general', 'General Reading')
    ]
    book_type = models.CharField(max_length=20, choices=book_type_choices)
    pledge_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title

from django.db import models

class BookDonation(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    book_title = models.CharField(max_length=200)
    book_type = models.CharField(
        max_length=50,
        choices=[('curriculum', 'Curriculum'), ('storybook', 'Storybook'), ('general', 'General Reading')]
    )
    delivery_option = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='book_donations/')
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book_title} by {self.donor_name}"

from django.db import models

class BookExchange(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('science', 'Science'),
        ('history', 'History'),
        ('romance', 'Romance'),
        ('selfhelp', 'Self Help'),
        ('biography', 'Biography'),
    ]

    DELIVERY_CHOICES = [
        ('dropoff', 'Drop off location'),
        ('pickup', 'Personal pick up'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    donor_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=100)  # Email or phone number
    location = models.CharField(max_length=100)  # City or town
    delivery_option = models.CharField(max_length=50, choices=DELIVERY_CHOICES)
    file = models.FileField(upload_to='book_exchange/')
    is_paid = models.BooleanField(default=False)
    delivery_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
