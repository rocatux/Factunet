from __future__ import unicode_literals
from django.db import models

from users.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=220)
    phoneSupplier = models.CharField(max_length=8, null=True)
    tipe_select = ( ('Principal','Principal'),
               ('Alterna','Alterna'),)
    tipe= models.CharField(
        max_length=10,
        choices=tipe_select,
        default= 'Principal',
        )
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 

# Modelo de cliente (comprador)
class Buyer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    surname = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=8, null=True)
    balances = models.PositiveIntegerField( null=True) #referencia a el saldo del cliente
    credit = models.PositiveIntegerField( null=True)
    discount = models.PositiveIntegerField( null=True)
    created_date = models.DateField(auto_now_add=True)
    dpi= models.CharField(max_length=24, null=False)

    def __str__(self):
        return '%s %s %s'%(self.name, self.surname, self.dpi)


class Addresses(models.Model):
    buyer_client = models.ForeignKey(Buyer, null = True, blank=True, on_delete = models.CASCADE)
    address = models.CharField(max_length=254, null = True)

    def __str__(self):
        return '%s %s'%(self.buyer_client, self.address)

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length = 254, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pendiente', 'Pendiente'),
        ('cancelar', 'Cancelar'),
        ('aprobado', 'Aprobado'),
        ('procesando', 'Procesando'),
        ('completado', 'Compleatado'),
        ('aumentar', 'Aumentar'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    adrres = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name