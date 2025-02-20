from .models import PledgedBook, Blog,BookClub,ContactMessage
from .models import BookDonation
from .models import BookExchange
from django.contrib.auth.models import User
from django import forms
from .models import ImpactData





class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']



class BookClubForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = ['school_name', 'county', 'students_count', 'patron_name', 'patron_contact']


class DynamicModelForm(forms.ModelForm):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.model = model
        self.fields.update(forms.fields_for_model(model))

    class Meta:
        model = None  # Placeholder, dynamically set later
        fields = '__all__'



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']


class BookDonationForm(forms.ModelForm):
    class Meta:
        model = BookDonation
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type', 'delivery_option', 'book_image']

class PledgedBookForm(forms.ModelForm):
    class Meta:
        model = PledgedBook
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type']

class BookExchangeForm(forms.ModelForm):
    class Meta:
        model = BookExchange
        fields = ['title', 'author', 'genre', 'donor_name', 'contact_details', 'location', 'delivery_option', 'image']



class ImpactDataForm(forms.ModelForm):
    class Meta:
        model = ImpactData
        fields = ['students_impacted', 'schools_reached', 'book_exchanges', 'books_donated']
