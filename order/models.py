from django.db import models
from user.models import User

class Order(models.Model):
	consecutive = models.IntegerField()
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	code = models.CharField(max_length = 15)
	product = models.CharField(max_length = 150)
	quanty = models.IntegerField()
	price = models.IntegerField()
	discount = models.IntegerField()
	date = models.DateField(auto_now_add= True)


	def __str__(self):
		return str(self.consecutive)+' '+str(self.user.name)


