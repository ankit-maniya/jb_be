from django.contrib import admin

from .models import Cuttingtypes

# Register your models here.


class CuttingType(admin.ModelAdmin):
    # list_display = ['id', 'u_name']
    list_display = ['userid', 'c_id', 'c_name', 'c_colorcode', 'c_price']


admin.site.register(Cuttingtypes, CuttingType)
