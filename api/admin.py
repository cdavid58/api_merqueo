from django.contrib import admin
from .models import Category, Subcategory, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','product','price']
    search_fields = ['code','product']

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product,ProductAdmin)