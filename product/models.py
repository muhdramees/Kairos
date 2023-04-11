from django.contrib.auth.models import User

from django.db import models
from account.models import EmailUser
import datetime
import os
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    slug = models.CharField(max_length=200, null=True, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    product_image = models.ImageField(upload_to='images', blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=False)
    original_price = models.FloatField(null=True, blank=False)
    selling_price = models.FloatField(null=True, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    trending = models.BooleanField(default=True, help_text="0=default, 1=Trending")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def sub_total(self):
        return self.product.selling_price*self.product_qty

class Wishlist(models.Model):
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=10, null=False)
    address = models.TextField(null=True)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatuses = (
        ('Pending', 'Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses, default='Completed')
    message = models.TextField(null=False)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no) 
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    status=models.CharField(max_length=150,default='Order Placed')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)
    

class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email},{self.phone},{self.address},{self.city},{self.state},{self.country},{self.pincode},"




class CategoryOffer(models.Model):
    category_name= models.OneToOneField(Category, on_delete=models.CASCADE)

    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)])
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

class ProductOffer(models.Model):
    product_name = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)])
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
