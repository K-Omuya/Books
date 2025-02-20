from django.contrib import admin
from .models import BookExchange, ContactMessage, BlogPost,BookClub,BookDonation,Impact,PledgedBook

admin.site.register(BookExchange)
admin.site.register(ContactMessage)
admin.site.register(BookDonation)
admin.site.register(PledgedBook)

admin.site.register(BookClub)
admin.site.register(BlogPost)
admin.site.register(Impact)
