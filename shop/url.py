from django.urls import path
from shop.views import home_page, about,login_user,logout_user

urlpatterns = [
    path('', home_page , name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user')
]
