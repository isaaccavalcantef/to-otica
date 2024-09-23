from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


#classes
from customers.models import Customers
from .models import Orders

# Create your views here.

class OrdersListView(ListView):
	model = Orders

class OrdersDetailView(DetailView):
	model = Orders

class OrdersCreateView(CreateView):
	model = Orders
	fields = ["product", "status","valor", "customer"]
	success_url = reverse_lazy("orders_list")

class OrdersUpdateView(UpdateView):
	model = Orders
	fields = ["product", "status","valor",  "customer"]
	success_url = reverse_lazy("orders_list")

class OrdersDeleteView(DeleteView):
	model = Orders
	success_url = reverse_lazy("orders_list")
	