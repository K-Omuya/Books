from django.contrib import admin
from .models import BookExchange, ContactMessage, BlogPost,BookClub,BookDonation,Impact,PledgedBook
from .models import ImpactData


admin.site.register(BookExchange)
admin.site.register(ContactMessage)
admin.site.register(BookDonation)
admin.site.register(PledgedBook)
admin.site.register(ImpactData)
admin.site.register(BookClub)
admin.site.register(BlogPost)





from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals
