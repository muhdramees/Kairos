from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Coupon(models.Model):
    coupon_name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(70)]
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    
