from django.db import models
from customers.models import Customers


class Orders(models.Model):
	product = models.CharField(
		verbose_name="Produto", max_length= 100, null=False, blank=False)
	status = models.CharField(
		verbose_name="Status", max_length= 100, null=False, blank=False)
	valor = models.DecimalField(max_length= 10, verbose_name=("Valor"), max_digits=10, decimal_places=2, default=0, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	customer = models.ForeignKey("customers.Customers", verbose_name=("Cliente"), null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.objects.all())