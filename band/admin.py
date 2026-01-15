from django.contrib import admin
from .models import BandMember, Album, Song

admin.site.register(BandMember)
admin.site.register(Album)
admin.site.register(Song)
