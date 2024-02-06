from django.contrib import admin
from . import models


admin.site.register(models.category)
admin.site.register(models.Customer)
admin.site.register(models.Products)
admin.site.register(models.Order)
