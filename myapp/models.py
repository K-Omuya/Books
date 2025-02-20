from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Change related_name to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Change related_name to avoid conflicts
        blank=True
    )




class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject




class Impact(models.Model):
    students_impacted = models.IntegerField()
    schools_reached = models.IntegerField()
    exchanges = models.IntegerField()
    books_donated = models.IntegerField()

    def __str__(self):
        return f"Impact Data (ID: {self.id})"

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models

class BookClub(models.Model):
    school_name = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    students_count = models.IntegerField()
    patron_name = models.CharField(max_length=255)
    patron_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.school_name


from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
    ]
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    donor_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    delivery_option = models.CharField(max_length=255, choices=[('drop_off', 'Drop Off'), ('personal_pickup', 'Personal Pickup')])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models

class BookExchange(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    donor_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=100)  # Email or phone
    location = models.CharField(max_length=255)  # City or town
    delivery_option = models.CharField(max_length=100, choices=[('Drop-off', 'Drop-off'), ('Personal Pick-up', 'Personal Pick-up')])
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.title
