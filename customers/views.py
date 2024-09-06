from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#classes
from .models import Customers

# Create your views here.

class CustomersListView(ListView):
	model = Customers

class CustomersCreateView(CreateView):
	model = Customers
	fields = ["firstName", "lastName", "cpf", "phone1","phone2"]
	success_url = reverse_lazy("customers_list")

class CustomersUpdateView(UpdateView):
	model = Customers
	fields = ["firstName", "lastName", "cpf", "phone1","phone2"]
	success_url = reverse_lazy("customers_list")

class CustomersDeleteView(DeleteView):
	model = Customers
	success_url = reverse_lazy("customers_list")
	