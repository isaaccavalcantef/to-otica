from django.db import models
from customers.models import Customers

	
# Create your models here.
class Cliente(models.Model):
	customer = models.ForeignKey("customers.Customers", verbose_name=("Cliente"), null=True, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.pk)


class Orders(models.Model):
	product = models.CharField(
		verbose_name="Produto", max_length= 100, null=False, blank=False)
	status = models.CharField(
		verbose_name="Status", max_length= 100, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	customer = models.ForeignKey("customers.Customers", verbose_name=("Cliente"), null=True, on_delete=models.CASCADE)
	
