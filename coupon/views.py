from django.shortcuts import render, redirect
from .models import*
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CouponForm
from django.contrib import messages

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