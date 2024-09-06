from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#classes
from .models import Orders

# Create your views here.

class OrdersListView(ListView):
	model = Orders

class OrdersCreateView(CreateView):
	model = Orders
	fields = ["product", "status", "date"]
	success_url = reverse_lazy("orders_list")

class OrdersUpdateView(UpdateView):
	model = Orders
	fields = ["product", "status", "date"]
	success_url = reverse_lazy("orders_list")

class OrdersDeleteView(DeleteView):
	model = Orders
	success_url = reverse_lazy("orders_list")
	