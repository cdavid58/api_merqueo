from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.CharField(max_length = 15)
	psswd = models.CharField(max_length = 20)
	block = models.BooleanField(default= False)
	verified = models.BooleanField(default = False)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

@receiver(post_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    print(f"El usuario con ID {instance.id} ha sido eliminado de la base de datos.")


class Shipping_Address(models.Model):
	address = models.CharField(max_length = 250)
	phone = models.CharField(max_length = 15)
