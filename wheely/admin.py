from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name','category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price',
                    'slug', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
