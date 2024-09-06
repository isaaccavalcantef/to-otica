from django.db import models

# Create your models here.
class Orders(models.Model):
	product = models.CharField(
		verbose_name="Produto", max_length= 100, null=False, blank=False)
	status = models.CharField(
		verbose_name="Status", max_length= 100, null=False, blank=False)
	date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	