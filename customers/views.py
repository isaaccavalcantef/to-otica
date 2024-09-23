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

class CustomersDetailView(DetailView):
	model = Customers
	def get_context_data(self, **kwargs):
		pk = self.kwargs['pk']
		orders = Orders.objects.all().filter(customer_id=pk)
		context = super(CustomersDetailView, self).get_context_data(**kwargs)
		context['Orders'] = orders
		context['pk'] = pk
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
	