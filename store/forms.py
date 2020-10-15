from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Order, Delivery, Addresses, Buyer, Supplier

#Form suplier#   formulario para proveeres

class SupplierForm(ModelForm):
    class Meta: 
        model = Supplier
        fields = '__all__'

    tipe = forms.Select(attrs={
        'class': 'form-control',
        'id': 'tipe',
    })    



    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'maxlength':'50',
        'placeholder': '',
        'autocomplete': 'off',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'maxlength':'220',
        'data-val': 'true',
        'placeholder': '',
        'autocomplete': 'off',
    }))
    phoneSupplier = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phoneSupplier',
        'maxlength':'8',
        'data-val': 'true',
        'placeholder': '',
        'autocomplete': 'off',
    }))
  

#Form Buyer# Formulario Para Clientes compradores
class BuyerForm(ModelForm):
    class Meta: 
        model = Buyer
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'maxlength':'120',
        'data-val': 'true',
        'placeholder': 'Ingrese su o sus nombres',
        'autocomplete':'off',
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'surname',
        'maxlength':'120',
        'data-val': 'true',
        'placeholder': 'Ingrese sus apellidos',
        'autocomplete':'off',
    }))

    dpi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'dpi',
        'maxlength':'24',
        'data-val': 'true',
        'placeholder': 'ingrese dpi sin espacios',
        'autocomplete':'off',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phone',
        'data-val': 'false',
        'maxlength':'8',
        'autocomplete':'off',
        'placeholder': '#',
    }))

    balances = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'balances',
        'data-val': 'false',
        'autocomplete':'off',
    }))

    credit = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'credit',
        'data-val': 'false',
        'autocomplete':'off',
    }))
    
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'discount',
        'data-val': 'false',
        'autocomplete':'off',
    }))


class AddressesForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = '__all__'

        widgets = {
            'buyer_client': forms.Select(attrs={'class': 'form-control', 'id': 'buyer_client', 'autocomplete': 'off'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address', 'autocomplete': 'off'})

        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'autocomplete':'off', 'maxlength':'120'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'id':'description', 'autocomplete':'off', 'maxlength':'254'}),
            'price' : forms.NumberInput(attrs={'class':'form-control', 'id':'price'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'adrres', 'product', 'design',  'color', 'buyer', 'quantity']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'adrres': forms.Select(attrs={'class': 'form-control', 'id': 'adrres'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'design': forms.TextInput(attrs={'class': 'form-control', 'id': 'design', 'autocomplete':'off'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color', 'autocomplete':'off'}),
            'buyer': forms.Select(attrs={'class': 'form-control select2', 'id': 'buyer', 'autocomplete':'off'}),
            'quantity' : forms.NumberInput(attrs={'class':'form-control', 'id':'quantity'})

        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name', 'autocomplete':'off'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']

        labels = {

        'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'autocomplete':'off'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'autocomplete':'off'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'autocomplete':'off'}),
        'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'autocomplete':'off'}),
        'password1': forms.TextInput(attrs={'class': 'form-control', 'id': 'password1', 'autocomplete':'off'}),
        'password2': forms.TextInput(attrs={'class': 'form-control', 'id': 'password2', 'autocomplete':'off'}),
        
        }
