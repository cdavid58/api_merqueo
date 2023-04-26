from django.db import models
from user import User

class Order(models.Model):
	consecutive = models.IntegerField()
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	code = models.IntegerField()
	product = models.CharField(max_length = 150)
	quanty = models.IntegerField()
	price = models.IntegerField()
	discount = models.IntegerField()


