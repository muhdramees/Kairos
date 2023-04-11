
from django.urls import path
from . import views

urlpatterns = [
        path('men/', views.men_product , name="men_product"),
        path('women/', views.women_product , name="women_product"),
        path('kid/', views.kid_product , name="kid_product"),

       


]