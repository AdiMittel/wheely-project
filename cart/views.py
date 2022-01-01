
from django.shortcuts import redirect, render, get_object_or_404, render, get_list_or_404
from django.views.decorators.http import require_POST
from wheely.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, qty=cd['qty'], override_qty=cd['override_qty'])
    return redirect('cart_detail')


def cart_delete(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})