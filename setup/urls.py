
from django.contrib import admin
from django.urls import path

from customers.views import CustomersListView, CustomersCreateView, CustomersUpdateView, CustomersDeleteView
from orders.views import OrdersListView, OrdersCreateView, OrdersUpdateView, OrdersDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),

	# Clientes
	path("", CustomersListView.as_view(), name="home"),
	path("create-customers", CustomersCreateView.as_view(), name="customers_create"),
	path("update-customers/<int:pk>", CustomersUpdateView.as_view(), name="customers_update"),
	path("delete-customers/<int:pk>", CustomersDeleteView.as_view(), name="customers_delete"),

	# Pedidos
	path("orders", OrdersListView.as_view(), name="orders_list"),
	path("create-orders", OrdersCreateView.as_view(), name="orders_create"),
	path("update-orders/<int:pk>", OrdersUpdateView.as_view(), name="orders_update"),
	path("delete-orders/<int:pk>", OrdersDeleteView.as_view(), name="orders_delete"),
]	
 