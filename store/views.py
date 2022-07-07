from venv import create
from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
  products = Product.objects.all()
  return render(request, 'store/store.html',{
    "products": products
  })

def cart(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem.set.all()
  else:
    items=[]
    
  context = {'items'}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)