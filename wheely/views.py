from typing import List
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImage
from django.urls import reverse_lazy
from django.views.generic import ListView
from cart.forms import CartAddProductForm
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
    context_object_name = 'products'
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

    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'listings/product.html', {'product': product, 'cart_product_form': cart_product_form})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request,'listings/by_category.html', {'category':category, 'products':product})

def contact(request):
    return render(request, 'cart/contact.html')