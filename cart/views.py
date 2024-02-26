from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from shop.models import Products
from django.contrib import messages
from django.http import JsonResponse,HttpResponse


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantity = cart.get_quantity()
    return render(request, 'cart_summery.html', {'cart_products': cart_products})



def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Products, id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity = len(cart)
        response=JsonResponse({'qty': cart_quantity})
        return response
    else:
        return JsonResponse({'error': 'Invalid request'}, status=200)


def remove_from_cart(request, cart_item_id):
    cart = Cart(request)
    cart.remove_item(int(cart_item_id))
    context = {
        'cart_products': cart.get_prods(),
        'quantity': cart.get_quantity(),
    }
    return render(request, 'category.html', context)
