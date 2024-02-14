from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Products
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart_summery.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')

        product = get_object_or_404(Products, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'product_name': product.name})
        return response


def cart_delete(request):
    pass  # Implement this function if you need to delete items from the cart

def cart_update(request):
    pass  # Implement this function if you need to update items in the cart
