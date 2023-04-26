from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import Order
from user.models import User

@api_view(['POST'])
def Create_Order(request):
	data = request.data
	user = User.objects.get(email = data['email'])
	try:
		order = Order.objects.filter(user = user).last()
	except Order.DoesNotExist:
		order = None

	Order(
		consecutive = 1 if order is None else order.consecutive + 1,
		user = data['user'],
		code = data['code'],
		product = data['product'],
		quanty = data['quanty'],
		price = data['price'],
		discount = data['discount']
	).save()

	return Response({})




