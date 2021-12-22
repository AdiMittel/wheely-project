from typing import List
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from .models import Product, SubCategory, Category, ProductImage
from django.urls import reverse_lazy
from django.views.generic import ListView
# Create your views here.

# def homepage(request):
#     return render(request, 'homepage.html')

class AllProducts(ListView):
    queryset = Product.objects.all()
    context_object_name = 'items'
    template_name = 'listings/shop.html'
    

    def productImage(self):
        queryset = ProductImage.objects.all
        context_object_name = 'product_images'

class Homepage(ListView):
    queryset = Product.objects.all()
    context_object_name = 'items'
    template_name = 'homepage.html'

class Footer(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'footer.html'

def about(request):
    return render(request, 'about.html')

class Categories(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'

class SubCategories(ListView):
    queryset = SubCategory.objects.all()
    context_object_name = 'subCategories'
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'listings/product.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'shop/listings/by_categoty', {'category':category, 'products':product})

# class Cart(ListView):
#     pass