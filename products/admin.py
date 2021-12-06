from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'price', 'product_image']
    list_editable = ['product_image', 'is_active', 'price']
    list_filter = ('category', 'is_active')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
