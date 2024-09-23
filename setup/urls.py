
from django.contrib import admin
from django.urls import path

from customers.views import CustomersListView, CustomersCreateView, CustomersUpdateView, CustomersDeleteView, CustomerOrdersView
from orders.views import OrdersListView, OrdersCreateView, OrdersUpdateView, OrdersDeleteView, OrdersDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
	path("", CustomersListView.as_view(), name="home"),

	# Clientes
	path("", CustomersListView.as_view(), name="customers_list"),
	path("detail-customer/<int:pk>", CustomerOrdersView.as_view(), name="customer_detail"),
	path("create-customers", CustomersCreateView.as_view(), name="customers_create"),
	path("update-customers/<int:pk>", CustomersUpdateView.as_view(), name="customers_update"),
	path("delete-customers/<int:pk>", CustomersDeleteView.as_view(), name="customers_delete"),

	# Pedidos
	path("orders", OrdersListView.as_view(), name="orders_list"),
	path("detail-orders/<int:pk>", OrdersDetailView.as_view(), name="orders_detail"),
	path("create-orders", OrdersCreateView.as_view(), name="orders_create"),
	path("update-orders/<int:pk>", OrdersUpdateView.as_view(), name="orders_update"),
	path("delete-orders/<int:pk>", OrdersDeleteView.as_view(), name="orders_delete"),
]	
 