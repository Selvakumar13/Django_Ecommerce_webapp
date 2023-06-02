from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class createorderform(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        exclude=['status']


class createproductform(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'})
        }
    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        price = cleaned_data.get('price')
        image_of_product = cleaned_data.get('image_of_product')
        description = cleaned_data.get('description')
        expiry_date=cleaned_data.get('expiry_date')
        if not product_name:
            self.add_error('product_name', 'Please enter the product name.')

        if len(product_name)<3:
            self._errors[ 'product_name' ] = self.error_class([ 'A minimum of 3 characters is required' ])

        if not price:
            self.add_error('price', 'Please enter the price.')

        if price<=0:
            self._errors[ 'price' ] = self.error_class([ 'price cant be negative' ])


        if not image_of_product:
            self.add_error('image_of_product', 'Please upload an image of the product.')

        if not description:
            self.add_error('description', 'Please enter the description.')

        if not expiry_date:
                self.add_error('expiry_date', 'Please enter the description.')

        return cleaned_data


class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


