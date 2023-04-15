
from django.urls import path
from . import views

urlpatterns = [
       # path('', views.index , name="index"),
       # path('home/', views.home , name="home"),
       path('', views.home , name="home"),
       path('product/<str:slug>', views.product_view, name="product_view"),
       path('product/<str:cate_slug>/<str:prod_slug>', views.item_view, name="item_view"),
       path('add-to-cart/', views.add_to_cart , name="add_to_cart"),
       path('cart/', views.view_cart , name="view_cart"),
       path('update-cart/', views.update_cart , name="update_cart"),
       path('delete-cart-item/', views.delete_cart_item , name="delete_cart_item"),
       path('wishlist/', views.wishlist , name="wishlist"),
       path('add-to-wishlist/', views.add_to_wishlist , name="add_to_wishlist"),
       path('delete-wishlist-item/', views.delete_wishlist_item , name="delete_wishlist_item"),
       path('cheakout/', views.cheakout, name='cheakout'),
       path('add-address/', views.add_address, name='add_address'),
       path('address-list/', views.address_list, name='address_list'),



       # path('apply-coupon/', views.apply_coupon, name='apply_coupon'),




       path('placeorder/', views.placeorder, name='placeorder'),
       path('proceed-to-pay/', views.proceed_to_pay, name='proceed_to_pay'),
       path('my-order/', views.my_order, name='my_order'),
       path('view-order/<str:t_no>', views.view_order, name='view_order'),
       path('product-list/', views.product_list, name='product_list'),
       path('search-product/', views.search_product, name='search_product'),
       
       




    
]