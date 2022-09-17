from django.contrib import admin

from .models import Loats

# Register your models here.


class LoatAdmin(admin.ModelAdmin):
    list_display = ['id', 'userid', 'partyid']


admin.site.register(Loats, LoatAdmin)
