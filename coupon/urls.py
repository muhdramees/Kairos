
from django.urls import path
from . import views

urlpatterns = [
       path('', views.coupon , name="coupon"),
       path('add-coupon/', views.add_coupon , name="add_coupon"),
       path('edit-coupon/<coupon_id>', views.edit_coupon , name="edit_coupon"),
       path('delete-coupon/<coupon_id>', views.delete_coupon , name="delete_coupon"),
       path('view-coupon/', views.view_coupon , name="view_coupon"),
       path('apply-coupon/', views.apply_coupon , name="apply_coupon"),
       path('remove-coupon/', views.remove_coupon , name="remove_coupon"),
    
]