from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import date

from product.models import Category,Product,Cart, Wishlist, Order, OrderItem, Profile
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from account.models import EmailUser
from django.contrib.sites.shortcuts import get_current_site
import random
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from coupon.models import Coupon
from product.forms import AddressForm
from coupon.forms import CheckoutForm
from datetime import date
from decimal import Decimal
# Create your views here.



# def index(request):
#     category = Category.objects.all()
#     context = {'category':category }
#     return render(request, "home/homepage.html", context)
    

    

def home(request):
   
    
    category = Category.objects.all()
    context = {'category':category }
    return render(request, "home/homepage.html", context)



def product_view(request, slug):

    if (Category.objects.filter(slug=slug, status=0)):
    
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'category':category, 'products':products}
        return render(request, "product/product-view-user.html", context)

    else:
        messages.warning(request, "No such Category found")
        return redirect("product_category")



def item_view(request, cate_slug, prod_slug):

    if(Category.objects.filter(slug=cate_slug, status=0)):

        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such Product found")
            return redirect('product_category')

    else:
        messages.error(request, "No such Category found")
        return redirect('product_category')

    return render(request, 'product/item-view.html', context)
    
  


def add_to_cart(request):

    if request.method == 'POST':
        
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_cheak = Product.objects.get(id=prod_id)

            if(product_cheak):

                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product is already in Cart"})

                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_cheak.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':"Product Added Successfully"})

                    else:
                        return JsonResponse({'status':"Only "+str(product_cheak.quantity)+" quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})

        else:
            return JsonResponse({'status':"Login to countinue"})

    
    return redirect('/')



@login_required(login_url='user_login')
def view_cart(request):
    cart = Cart.objects.filter(user=request.user)


    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price*item.product_qty
        
    
    
    
    
    
    

    context = {'cart': cart, 'total_price':total_price}
    return render(request, 'product/cart.html', context)



def update_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))

        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            
            return JsonResponse({'status':"Updated Succesfully"})
        







def delete_cart_item(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))

        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id = prod_id, user=request.user)
            cartitem.delete()

        return JsonResponse({'status': "Deleted Succesfully"})
    return redirect('/')



    
@login_required(login_url='user_login')
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request, 'product/wishlist.html', context)


def add_to_wishlist(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)

            if(product_check):

                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product already in wishlist"})

                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product added to wishlist"})

            else:
                return JsonResponse({'status':"No such product found"})

        else:
            return JsonResponse({'status':"Login to continue"})

    return redirect("/")


def delete_wishlist_item(request):

    if request.method == "POST":

        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.filter( user=request.user, product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product removed from wishlist"})

            else:
                return JsonResponse({'status': "Product not found in wishlist"})

        else:
            return JsonResponse({'ststus':"Login to countinue"})

    return redirect('/')


def cheakout(request):
    # rawcart = Cart.objects.filter(user = request.user)
    # coupon = Coupon.objects.all()
    # profile = Profile.objects.all()
    # form = CheckoutForm
    
    # for item in rawcart:
    #     if item.product_qty > item.product.quantity:
    #         # Cart.objects.delete(id=item.id)
    #         cheakout_item = Cart.objects.filter(id = item.id)
    #         cheakout_item.delete()

    # cartitems = Cart.objects.filter(user = request.user)
    # total_price = sum(item.product.selling_price * item.product_qty for item in cartitems)
    # discounted_price = total_price
    
    
    # userprofile = Profile.objects.filter(user = request.user).first()
    

    # context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile, 'coupon':coupon, 'profile':profile, 'form':form}
    # return render(request, 'product/cheakout.html', context)
    coupon_discount = 0
    raw_cart = Cart.objects.filter(user=request.user)
    profile = Profile.objects.all()
    coupon = None
    form = CheckoutForm(request.POST or None)

    if 'coupon' in request.session:
        coupon = request.session['coupon']


    if request.method == 'POST':
        if form.is_valid():
            coupon_code = form.cleaned_data('coupon_code')
            if coupon_code:
                try:
                    coupon = Coupon.objects.get(code=coupon_code)
                    request.session['coupon'] = {
                        'id':coupon.id,
                        'code':coupon.code,
                        'discount':coupon.discount,
                    }
                    messages.success(request, f"Coupon code '{coupon.code}' applied!")

                except Coupon.DoesNotExist:
                    messages.error(request, "Invalid coupon code!")
            else:
                request.session.pop('coupon', None)


    for item in raw_cart:
        if item.product_qty > item.product.quantity:
            item.delete()
    
    coupons = Coupon.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(coupon_discount)
    total = sum([item.product.selling_price * item.product_qty for item in cart_items])
    total_price = total

    # if coupons:
    #     print(total,"!!!!!!!!!!!")
    #     discount = coupon['discount']
    #     total_price = total * (discount/100)

    #     print("TTTTTTTTTTTTTTTTTTT", total_price)
    # else:
    #     print(total,"@@@@@@@@@@@")
    #     total_price = total
    #     print("iiiiiiiiiiiiiiiiii",total_price)

    # if coupon:

    #     total_price -= total_price * (coupon.discount/100)

    print(total_price,"**************************")

    
    context = {
        'cart_items':cart_items,
        'total':total,
        'total_price':total_price,
        'profile':profile,
        'coupon':coupon,
        'form':form,
        'coupons':coupons
    }
    return render(request, 'product/cheakout.html', context)



# add adress

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cheakout")
    else:
        form = AddressForm()
    return redirect(request, 'product/add-address.html', {'form':form})


def address_list(request):
    addresses = Profile.objects.all()
    return render(request, 'product/address-list.html', {'addresses':addresses})

        

# apply coupon

def apply_coupon(request):
    print("Apply Coupon")
    coupon_id = request.POST.get('coupon_code')
    print("##############",coupon_id)
    if request.method == 'POST':
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        coupon_id = request.POST.get('coupon_code')
        if coupon_id:
            print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
            try:
                coupon = Coupon.objects.get(id=coupon_id)
                request.session['coupon'] = {
                    'id':coupon.id,
                    'code':coupon.code,
                    'discount':coupon.discount,
                }
                print(coupon.discount)
                
                messages.success(request, f"Coupon code '{coupon.code}' applied!")
                
            except Coupon.DoesNotExist:
                messages.error(request, "Invalid coupon code!")



        # total = 0 
        # coupon_id = request.POST.get('coupon_code')
        # coupon = Coupon.objects.get(id=coupon_id)
        # print(coupon.coupon_name)
        # if Coupon.objects.filter(id=coupon_id).exists():
        #     c_exists = True
        #     today = date.today()
        #     if coupon.valid_from <= today and coupon.valid_to >= today:
        #         total -= coupon.discount
        else:
            request.session.pop('coupon', None)
                
    return redirect("cheakout")
    



def placeorder(request):
    if request.method == 'POST':

        currentuser = EmailUser.objects.filter(id = request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user = request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user = request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price

        trackno = 'kairos'+str(random.randint(11111111,99999999))
        while Order.objects.filter(tracking_no = trackno) is None:
            trackno = 'kairos'+str(random.randint(11111111,99999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user = request.user)
        for items in  neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity = item.product_qty
            )

            # To Decrese the product quantity from available stock

            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # To clear the product in user cart

        Cart.objects.filter(user = request.user).delete()

        messages.success(request, "Your order has been placed successully")

        payMode = request.POST.get('payment_mode')
        if (payMode == "Paid by Razorpay"):
            return JsonResponse({'status' : "Your order has been placed successully"}) 

    return redirect('/')


def proceed_to_pay(request):
    cart = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty

    return JsonResponse({
        'total_price':total_price
    })

def my_order(request):
    orders = Order.objects.filter(user = request.user)
    context = {'orders': orders}
    return render(request, "product/my-order.html", context)

def view_order(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user = request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems }
    return render(request, "product/view-order.html", context)

def product_list(request):
    products = Product.objects.filter(status = 0).values_list('name', flat=True)
    productList = list(products)
    return JsonResponse(productList, safe=False)

def search_product(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains = searchedterm).first()

            if product:
                return redirect("/product/"+product.category.slug+"/"+product.slug)
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))




