from django.shortcuts import render, redirect
from .models import*
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CouponForm
from django.contrib import messages
import datetime
from django.http import HttpResponse,JsonResponse



# Create your views here.


def coupon(request):
    coupon_list = Coupon.objects.all()
    paginator = Paginator(coupon_list, 3)
    page = request.GET.get('page')
    paged_coupon_list = paginator.get_page(page)
    return  render(request,'coupon/coupon.html',{
        'coupon':paged_coupon_list
    })

def add_coupon(request):
    form = CouponForm()
    if request.method == 'POST':
        form = CouponForm(request.POST)
        discount = form.data['discount']

        if int(discount) <= 70:

            if form.is_valid():
                form.save()
                return redirect('coupon')
            else:
                messages.error(request, 'Already Exists!!')
                return redirect('add_coupon')
        else:
            messages.error(request, 'Percentage should be less than or equal to 70')
            return redirect('add_coupon')
    context = {
        'form':form
    }
    return render(request, 'coupon/add-coupon.html', context)

def edit_coupon(request, coupon_id):
    coupon = Coupon.objects.get(pk=coupon_id)
    form = None
 
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=coupon)

        if form.is_valid():
            form.save()
            return redirect('coupon')
    else:
        form = CouponForm(instance=coupon)
    
    context = {
        'form':form,
        'coupon_id':coupon_id
    }

    return render(request, 'coupon/edit-coupon.html', context)


def delete_coupon(request, coupon_id):
    dlt = Coupon.objects.get(pk=coupon_id)
    dlt.delete()
    messages.success(request, 'Your Coupon has been deleted')
    return redirect('coupon')


def view_coupon(request):
    coupon = Coupon.objects.all()
    return render(request, 'coupon/view-coupon.html', {'coupon':coupon})

def apply_coupon(request):
    
    print("coupon : ")
    d   = datetime.datetime.today()
    now = datetime.date(d.year,d.month,d.day)
    print(now)
    code=request.GET.get('code')
    total=float(request.GET.get('grand_total'))

    print("code>>>>>>>>>>  :",code)
    print('total ; ',total)
 
    coup_discount=0

    coupon=Coupon.objects.all()
    verify="nil"
    for i in coupon:
        print(i)
        print(".............>>>>>>>>>>>>>>>>>>>>.............")
        if code ==  i.code:
            print(" if ill keri.........")
            verify=i.code
            print("verifyyyy",verify)
    
    if verify == "nil":
        return redirect('checkout')
    
    coup=Coupon.objects.get(code=verify)
    
    print("c :::::::",coup)
    print("valid from :",coup.valid_from)
    print("valid to : ",coup.valid_to)
    if now >= coup.valid_from and now <= coup.valid_to:
        coup.active=True
        print("date /////// ") 
        
        # coup_price= float(total) - coup.limited_price
        # print("coupon price",coup_price)
        discount=total - (total*coup.discount)/100
        print(discount)
        # if coup_price  < discount :
            
        #     new_price = coup_price+tax
        #     print("new_price : ",new_price)
        #     coup_discount = coup.limited_price
        
        new_price = discount 
        print("coupon koiiiiii : ",new_price)
        coup_discount=(total*coup.discount)/100
        coup.save()

        request.session['new_price']=new_price
        request.session['coupon'] = verify
        request.session['coup_discount'] = coup_discount
        print("lasttt")
        print(new_price,"#############################################")
        return JsonResponse({
            'grand_total':new_price,
            'Coupon':coup_discount,
            'Coupon_code':verify,
        }) 
    
    else:
        coup.active=False
        coup.save()
        print(' ]]]]]]]]]]]]]]]]]]]]]]]]]]]]  ')
        messages.error("Coupon is not valid !!")
        return JsonResponse({
            'grand_total':total,
            'Coupon':coup_discount,
            'Coupon_code':'Coupon is not valid !!',


        })
    
def remove_coupon(request):
    code=request.session['coupon']
    print("coupon code",code)
    request.session.pop('coupon',None)
    request.session.pop('new_price',None)
    request.session.pop('coup_discount',None)
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))
    
