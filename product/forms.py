from django import forms
from . models import Product, Category, CategoryOffer, ProductOffer, Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name','product_image','quantity','original_price','selling_price','status')





class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','image','image',)




class CategoryOfferForm(forms.ModelForm):
    class Meta:
        model = CategoryOffer
        fields = ('category_name','discount','start_date','end_date')
        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryOfferForm, self).__init__(*args, **kwargs)
        
        self.fields['discount'].widget.attrs['placeholder'] = 'Enter the discount percentage'


    # additional form validation and customization if needed

class ProductOfferForm(forms.ModelForm):
    class Meta:
        model = ProductOffer
        fields = ('product_name','discount','start_date','end_date')
        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductOfferForm, self).__init__(*args, **kwargs)
        
        self.fields['discount'].widget.attrs['placeholder'] = 'Enter the discount percentage'
    

class AddressForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','phone','address','city','state','country','pincode',]