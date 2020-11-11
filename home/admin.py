from django.contrib import admin
from .models import *
# Register your models here.

class KleeAdmin(admin.ModelAdmin):
    list_display=('name','date')
admin.site.register(Klee, KleeAdmin)