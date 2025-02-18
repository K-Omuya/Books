from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



class BookClub(models.Model):
    SCHOOL_CHOICES = [
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondary School'),
        ('Other', 'Other'),
    ]

    school_name = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    no_of_students = models.PositiveIntegerField()
    patron_name = models.CharField(max_length=255)
    patron_contact = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.school_name} - {self.county}"





class BookPledge(models.Model):
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    pledged_books = models.TextField()
    date_pledged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - {self.date_pledged.strftime('%Y-%m-%d')}"


class BookDonation(models.Model):
    BOOK_TYPES = [
        ('curriculum', 'Curriculum Books'),
        ('storybooks', 'Storybooks'),
        ('general', 'General Reading Books'),
    ]

    DELIVERY_OPTIONS = [
        ('drop_off', 'Drop off at nearest school book club'),
        ('pickup', 'Request for pickup (if available)'),
    ]

    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    book_title = models.CharField(max_length=255)
    book_image = models.ImageField(upload_to='donated_books/')
    book_type = models.CharField(max_length=20, choices=BOOK_TYPES)
    delivery_option = models.CharField(max_length=20, choices=DELIVERY_OPTIONS)
    date_donated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book_title} by {self.donor_name}"



class BookExchange(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('education', 'Educational'),
        ('biography', 'Biography'),
        ('fantasy', 'Fantasy'),
        ('history', 'History'),
        ('mystery', 'Mystery'),
        ('science', 'Science'),
    ]

    DELIVERY_OPTIONS = [
        ('drop_off', 'Drop off at location'),
        ('personal_pickup', 'Personal pick-up'),
    ]

    donor_name = models.CharField(max_length=255)
    email_or_phone = models.CharField(max_length=100)
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    location = models.CharField(max_length=100)
    delivery_option = models.CharField(max_length=20, choices=DELIVERY_OPTIONS)
    book_image = models.ImageField(upload_to='exchange_books/')
    date_added = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book_title} by {self.author}"
