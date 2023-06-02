from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__( self ):
        return self.name

class Product(models.Model):

    PRODUCT_TYPE=[
        ('brand new','Brand New'),
        ('second hand','Second Hand'),
        ('refurbished', 'Refurbished'),

    ]

    CATEGORIES  =[
        ('clothing','Clothing'),
        ('music','Music'),
        ('shoes','Shoes'),
    ]

    product_name=models.CharField(max_length=100)
    product_type=models.CharField(max_length=20,choices=PRODUCT_TYPE)
    price=models.DecimalField(max_digits=8,decimal_places=3)
    category=models.CharField(max_length=20,choices=CATEGORIES)
    image_of_product = models.ImageField(null=True, blank=True)
    description=models.TextField()
    expiry_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.product_name

class Order(models.Model):
    product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING')

    def __str__( self ):
        return f"Order {self.pk}"
