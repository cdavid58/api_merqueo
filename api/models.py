from django.db import models
import os, binascii

class Category(models.Model):
	name = models.CharField(max_length= 80)
	active = models.BooleanField(default = True)

	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length = 80)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

class Product(models.Model):
	code = models.CharField(max_length = 20,unique=True,default = str(binascii.b2a_hex(os.urandom(7)))[2:-1])
	product = models.CharField(max_length = 150)
	price = models.FloatField()
	discount = models.FloatField()
	description = models.TextField(null=True, blank=True)
	img = models.ImageField(upload_to = "Product")
	subcategory = models.ForeignKey(Subcategory, on_delete = models.CASCADE)


	def Total_Discount(self):
		return self.price - (self.price * (self.discount / 100))

	def __str__(self):
		return self.product