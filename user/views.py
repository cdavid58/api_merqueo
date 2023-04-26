from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import User


@api_view(['POST'])
def Create_User(request):
	data = request.data
	result = False
	try:
		user = User.objects.get(email = data['email'])
	except Exception as e:
		user = None
		print(e)

	if user is None:
		User(
			name = data['name'],
			email = data['email'],
			phone = data['phone'],
			psswd = data['psswd']
		).save()
		result = True
	return Response({'result':result})


@api_view(['POST'])
def Login(request):
	data = request.data
	message = "Usuario o contraseña incorrecta"
	result = False
	try:
		user = User.objects.get(email = data['email'], psswd = data['psswd'])
		data = {
			"name": user.name,
			"email" : user.email,
			"phone" : user.phone,
			"psswd" : user.psswd
		}
		result = True
		message = "success"
	except Exception as e:
		message = str(e)

	return Response({ 'result':result, 'message':message,'data':data })