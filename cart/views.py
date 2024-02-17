from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Products
from django.http import JsonResponse,HttpResponse

def cart_summary(request):
    return render(request, 'cart_summery.html')


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Products, id=product_id)
        cart.add(product=product)
        cart_quantity = len(cart)
        return JsonResponse({'qty': cart_quantity})
    else:
        return JsonResponse({'error': 'Invalid request'} , status=200)

#
def cart_delete(request):
    pass
def cart_update(request):

    pass