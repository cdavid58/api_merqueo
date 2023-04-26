from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.CharField(max_length = 15)
	psswd = models.CharField(max_length = 20)
	block = models.BooleanField(default= False)
	verified = models.BooleanField(default = False)

	def __str__(self):
		return self.name