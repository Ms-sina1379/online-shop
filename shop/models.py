from django.db import models
import  datetime


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
        firs_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        email = models.EmailField()
        phone = models.CharField(max_length=20)
        password = models.CharField(max_length=20)

        def __str__(self):
            return self.name

class Products(models.Model):
            name = models.CharField(max_length=20)
            description = models.TextField(blank=True)
            category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
            price = models.DecimalField(max_digits=20, decimal_places=2)
            picture = models.ImageField(upload_to='upload/Product/')

            is_sale = models.BooleanField(default=False)
            sale_price = models.DecimalField( default= 0 ,max_digits=20,decimal_places=2)

            def __str__(self):
                return self.name

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
     return self.product