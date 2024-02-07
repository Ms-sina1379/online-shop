
from django.contrib import admin
from django.urls import path,include
from shop.views import home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("",home_page,name="home"),
    path("shop/",include('shop.urls')),
    path("cart/",include('cart.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

