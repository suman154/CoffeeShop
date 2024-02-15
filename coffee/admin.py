from django.contrib import admin
from .models import coffee
# Register your models here.
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')



admin.site.register(coffee, CoffeeAdmin)