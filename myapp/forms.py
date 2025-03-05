from django import forms
from .models import Book, Pledge, BookClub, BookDonation


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'book_type', 'drop_off_location']

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['name', 'email', 'book_count']

from django import forms
from .models import BookClub
class BookClubForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = ['school_name', 'county', 'students_count', 'patron_name', 'patron_contact']

from .models import PledgedBook,BookExchange

class PledgedBookForm(forms.ModelForm):
    class Meta:
        model = PledgedBook
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type']


class BookDonationForm(forms.ModelForm):
    class Meta:
        model = BookDonation
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type', 'delivery_option', 'book_image']



from django import forms
from .models import BookExchange

class BookExchangeForm(forms.ModelForm):
    class Meta:
        model = BookExchange
        fields = ['genre', 'title', 'author', 'donor_name', 'contact_details', 'location', 'delivery_option', 'file']
