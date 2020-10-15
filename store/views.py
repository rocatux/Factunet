from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Buyer,
    Product,
    Order,
    Delivery,
    Addresses

)
from .forms import (
    SupplierForm,
    BuyerForm,
    ProductForm,
    OrderForm,
    DeliveryForm,
    AddressesForm,
    RegisterForm
)

# Supplier views----------------------------------------------------
class create_supplier(CreateView):
    template_name='store/create_supplier.html'
    form_class=SupplierForm
    success_url=reverse_lazy('supplier-list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'
    paginate_by = 6

    def get_queryset(self):
        return Supplier.objects.all().order_by('id')

class delete_supplier(DeleteView):
    model = Supplier
    template_name = 'store/delete_supplier.html'
    success_url = reverse_lazy('supplier-list')

class edit_supplier(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'store/edit_supplier.html'
    success_url = reverse_lazy('supplier-list')


# Buyer views---------------------------------------------------------
class create_buyer(CreateView):
    template_name='store/create_buyer.html'
    form_class=BuyerForm
    success_url=reverse_lazy('buyer-list')

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'
    paginate_by = 6

    def get_queryset(self):
        return Buyer.objects.all().order_by('id')

# delete buyer
class delete_buyer(DeleteView):
    model = Buyer
    template_name = 'store/delete_buyer.html'
    success_url = reverse_lazy('buyer-list')

# Address-------------------------------------------------------------------------
class Create_Addresses(CreateView):
    template_name = 'store/create_addresses.html'
    form_class=AddressesForm
    success_url=reverse_lazy('buyer-list')

# Product views-------------------------------------------------------------------
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all().order_by('id')

class delete_product(DeleteView):
    model = Product
    template_name = 'store/delete_product.html'
    success_url = reverse_lazy('product-list')

class edit_product(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/edit_product.html'
    success_url = reverse_lazy('product-list')



# Order views------------------------------------------------------------------------
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            buyer = forms.cleaned_data['buyer']
            adrres = forms.cleaned_data['adrres']
            quantity = forms.cleaned_data['quantity']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                adrres=adrres,
                quantity=quantity,
                status='pendiente'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'
    context_object_name = 'order'
    paginate_by = 6

    def get_queryset(self):
        return Order.objects.all().order_by('id')

class delete_order(DeleteView):
    model = Order
    template_name = 'store/delete_order.html'
    success_url = reverse_lazy('order-list')

class edit_order(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'store/edit_order.html'
    success_url = reverse_lazy('order-list')


# Delivery views---------------------------------------------------------------------------
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'
    paginate_by = 6

    def get_queryset(self):
        return Delivery.objects.all().order_by('id')

class delete_delivery(DeleteView):
    model = Delivery
    template_name = 'store/delete_delivery.html'
    success_url = reverse_lazy('delivery-list')

class edit_delivery(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'store/edit_delivery.html'
    success_url = reverse_lazy('delivery-list')

class create_user(CreateView):
    model = User
    template_name='store/create_user.html'
    form_class= RegisterForm
    success_url = reverse_lazy('delivery-list')