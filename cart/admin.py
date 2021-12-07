from django.contrib import admin
from .models import Cart


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_editable = ('quantity',)
    list_per_page = 20
    search_fields = ('user', 'product')


admin.site.register(Cart, CartAdmin)