from django import forms
from .models import Coupon




class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            'coupon_name',
            'code',
            'discount',
            'valid_from',
            'valid_to',
        ]

        widgets = {
            'valid_from': forms.widgets.DateInput(attrs={'type': 'date'}),
            'valid_to': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['discount'].widget.attrs['placeholder'] = 'Enter the discount percentage'

class CheckoutForm(forms.Form):
    coupon_code = forms.CharField(required=False)