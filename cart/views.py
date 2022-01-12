
from os import remove
from django.shortcuts import redirect, render, get_object_or_404, render, get_list_or_404
from django.views.decorators.http import require_POST
from wheely.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    delete_from_cart = request.GET.get('delete_from_cart','')
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product, qty=int(cd['qty']), override_qty=cd['override'])
    if delete_from_cart:
        cart.delete(delete_from_cart)
    return redirect('cart_details')


def cart_delete(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product_id)
    return redirect('cart_details')

# def cart_update(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.update(product_id)
#     return redirect('cart_details')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

