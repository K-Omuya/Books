from django import forms
from .models import BlogPost
from django import forms
from .models import ContactMessage
from django import forms
from .models import BookClub
from django import forms
from .models import BookExchange

from django import forms
from .models import BookPledge, BookDonation




class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']



class BookClubForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = ['school_name', 'county', 'no_of_students', 'patron_name', 'patron_contact']



class BookPledgeForm(forms.ModelForm):
    class Meta:
        model = BookPledge
        fields = ['donor_name', 'donor_email', 'pledged_books']


class BookDonationForm(forms.ModelForm):
    class Meta:
        model = BookDonation
        fields = ['donor_name', 'donor_email', 'book_title', 'book_image', 'book_type', 'delivery_option']

class BookPledgeForm(forms.ModelForm):
    class Meta:
        model = BookPledge
        fields = ['donor_name', 'donor_email', 'pledged_books']


class BookDonationForm(forms.ModelForm):
    class Meta:
        model = BookDonation
        fields = ['donor_name', 'donor_email', 'book_title', 'book_image', 'book_type', 'delivery_option']

class BookExchangeForm(forms.ModelForm):
    class Meta:
        model = BookExchange
        fields = ['donor_name', 'email_or_phone', 'book_title', 'author', 'genre', 'location', 'delivery_option', 'book_image']
