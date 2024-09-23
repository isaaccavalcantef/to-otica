from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


#classes
from .models import Customers
from orders.models import Orders

# Create your views here.


class CustomersListView(ListView):
	model = Customers

class CustomerOrdersView(DetailView):
	model = Customers
	fields = ["firstName", "lastName", "cpf", "phone1","phone2"]
	def get_context_data(self, **kwargs):
		pk = self.kwargs['pk']
		customers = Customers.objects.filter(id=pk).values
		orders = Orders.objects.filter(customer_id=pk)
		ordersCount = Orders.objects.filter(customer_id=pk).count
		ordersSoma = Orders.objects.filter(customer_id=pk)
		soma = Orders.objects.filter(customer_id=pk).annotate(sum('valor'))
		context = super(CustomerOrdersView, self).get_context_data(**kwargs)
		context['Orders'] = orders
		context['customers'] = customers
		context['pk'] = pk
		context['count'] = ordersCount
		context['sum'] = soma
		return context


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
	