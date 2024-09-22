from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#classes
from customers.models import Customers
from .models import Orders

# Create your views here.

class OrdersListView(ListView):
	model = Orders
	
# def OrdersCustomersListView(request):
# 	model = Customers
# 	orders = Orders.objects.all
# 	return render(request, "orders/templates/orders/orders_list.html", {"orders": orders})
	

class OrdersCreateView(CreateView):
	model = Orders
	fields = ["product", "status", "customer"]
	success_url = reverse_lazy("orders_list")

class OrdersUpdateView(UpdateView):
	model = Orders
	fields = ["product", "status", "customer"]
	success_url = reverse_lazy("orders_list")

class OrdersDeleteView(DeleteView):
	model = Orders
	success_url = reverse_lazy("orders_list")
	