from django.db import models

# Create your models here.
class Customers(models.Model):
	firstName = models.CharField(
		verbose_name="Primeiro Nome", max_length= 100, null=False, blank=False)
	lastName = models.CharField(
		verbose_name="Ultimo Nome", max_length= 100, null=False, blank=False)
	cpf = models.CharField(
		verbose_name="CPF", max_length= 11, null=False, blank=False)
	phone1 = models.CharField(
		verbose_name="Telefone 1", max_length= 11, null=False, blank=False)
	phone2 = models.CharField(verbose_name="Telefone 2", max_length= 11)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

	def __str__(self):
		a = str(self.firstName)
		b = str(self.lastName)
		return str(a+" "+b)
	
	