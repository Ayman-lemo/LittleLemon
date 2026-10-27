from django.contrib import admin
from .models import Booking, Category, Menu, MenuItem

admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(MenuItem)