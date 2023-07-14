from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username']

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

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            if self.user:
                customer = Customer.objects.get(user=self.user)
                instance.customer = customer
                instance.save()
        return instance


class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


