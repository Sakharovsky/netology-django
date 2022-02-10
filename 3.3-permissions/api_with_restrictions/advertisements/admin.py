from django.contrib import admin

from advertisements.models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'status', 'creator']
    list_display = ('title', 'description', 'status', 'creator', 'created_at', 'updated_at')

admin.site.register(Advertisement, AdvertisementAdmin)