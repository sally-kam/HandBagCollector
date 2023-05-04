from django.contrib import admin
from .models import Handbag, Worn, Item

# Register your models here.
admin.site.register(Handbag)
admin.site.register(Worn)
admin.site.register(Item)
