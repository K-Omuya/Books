from django.contrib import admin
from .models import BookExchange, ContactMessage, BlogPost,BookClub,BookPledge,BookDonation

admin.site.register(BookExchange)
admin.site.register(ContactMessage)
admin.site.register(BookDonation)
admin.site.register(BookPledge)
admin.site.register(BookClub)
admin.site.register(BlogPost)
