from django.urls import path
from shop.views import home_page, about, login_user, logout_user, register_user, category, product,search


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('product/<int:pk>/', product, name='product'),
    path('logout/', logout_user, name='logout_user'),
    path('search/', search, name='search'),
    path('category/<str:cat>/',category, name='Category')
]
