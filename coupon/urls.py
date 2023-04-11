
from django.urls import path
from . import views

urlpatterns = [
       path('', views.coupon , name="coupon"),
       path('add-coupon/', views.add_coupon , name="add_coupon"),
       path('edit-coupon/<coupon_id>', views.edit_coupon , name="edit_coupon"),
       path('delete-coupon/<coupon_id>', views.delete_coupon , name="delete_coupon"),
]