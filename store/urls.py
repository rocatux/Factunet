from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import (
    create_supplier,
    create_buyer,
    create_product,
    create_order,
    create_delivery,
    Create_Addresses,
    create_user,

    delete_buyer,
    delete_supplier,
    delete_product,
    delete_order,
    delete_delivery,

    edit_supplier,
    edit_product,
    edit_order,
    edit_delivery,

    SupplierListView,
    BuyerListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
)

urlpatterns = [
    path('create-supplier/', login_required(create_supplier.as_view()), name='create-supplier'),
    path('create-buyer/', login_required(create_buyer.as_view()), name='create-buyer'),
    path('create-addresses/', login_required(Create_Addresses.as_view()), name='create-addresses'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),
    path('create-user/', create_user.as_view(), name='create-user'),

    path('delete-buyer/<int:pk>/',login_required(delete_buyer.as_view()), name='delete-buyer'),
    path('delete-supplier/<int:pk>/',login_required(delete_supplier.as_view()), name='delete-supplier'),
    path('delete-product/<int:pk>/',login_required(delete_product.as_view()), name='delete-product'),
    path('delete-order/<int:pk>/',login_required(delete_order.as_view()), name='delete-order'),
    path('delete-delivery/<int:pk>/',login_required(delete_delivery.as_view()), name='delete-delivery'),

    path('edit-supplier/<int:pk>/',login_required(edit_supplier.as_view()), name='edit-supplier'),
    path('edit-product/<int:pk>/',login_required(edit_product.as_view()), name='edit-product'),
    path('edit-order/<int:pk>/',login_required(edit_order.as_view()), name='edit-order'),
    path('edit-delivery/<int:pk>/',login_required(edit_delivery.as_view()), name='edit-delivery'),

    path('supplier-list/', login_required(SupplierListView.as_view()), name='supplier-list'),
    path('buyer-list/', login_required(BuyerListView.as_view()), name='buyer-list'),
    path('product-list/', login_required(ProductListView.as_view()), name='product-list'),
    path('order-list/', login_required(OrderListView.as_view()), name='order-list'),
    path('delivery-list/', login_required(DeliveryListView.as_view()), name='delivery-list'),
]