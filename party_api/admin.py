from django.contrib import admin

from .models import Partys

# Register your models here.


class PartysAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'p_billingname', 'p_mobile']


admin.site.register(Partys, PartysAdmin)
