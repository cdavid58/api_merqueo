from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import Order
from user.models import User

@api_view(['POST'])
def Create_Order(request):
	data = request.data
	user = User.objects.get(email = data[0]['email'])
	try:
		order = Order.objects.filter(user = user).last()
		try:
			n = order.consecutive + 1
		except Exception as e:
			n = 1
	except Order.DoesNotExist:
		order = None

	for i in range(len(data)):
		Order(
			consecutive = 1 if order is None else n,
			user = user,
			code = data[i]['code'],
			product = data[i]['product'],
			quanty = data[i]['quanty'],
			price = data[i]['price'],
			discount = data[i]['discount']
		).save()

	return Response({'consecutive':n})

@api_view(['POST'])
def Download_Order(requests):
    return Response([
        {
            "numero": i.consecutive,
            "codigo":i.code,
            "producto":i.product,
            "cantidad":i.quanty,
            "precio":i.price,
            "descuento":i.discount,
            "total":i.Total_Order(),
            "nombre":i.user.name,
            "telefono":i.user.phone,
            "email":i.user.email
        }
        for i in Order.objects.filter(download = False)
    ])

@api_view(['POST'])
def Update_State(request):
    data = request.data
    try:
        o = Order.objects.filter(consecutive = data['number'],user = User.objects.get(email = data['email']))
        for i in o:
            i.download = True
            i.save()
    except Exception:
        pass
    return Response(True)




