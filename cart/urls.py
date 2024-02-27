from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_summary, name='cart_summery'),
    path('add/', views.cart_add, name='cart_add'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='delete_from_cart'),

]
