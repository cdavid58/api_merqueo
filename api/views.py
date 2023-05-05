from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Category, Subcategory, Product
import os.path as path, sqlite3
from from_number_to_letters import Thousands_Separator

@api_view(['POST'])
def Create_Category(request):
	result = False
	try:
		c = Category.objects.get(name = request.data['name'])
	except Exception as e:
		c = None
	if c is None:
		Category(
			name = request.data['name']
		).save()
		result = True
	return Response({'result':result})


@api_view(['POST'])
def Create_SubCategory(request):
	data = request.data
	run = False
	try:
		c = Category.objects.get(name = request.data['category'], active = True)
		subc= Subcategory.objects.get(name = data['subcategory'], category = c)
		run = False
	except Exception as e:
		run = True

	if run:
		Subcategory(
			name = data['subcategory'],
			category = c
		).save()
		result = True
	return Response(result)

@api_view(['POST'])
def Create_Product(request):
	data = request.data
	Product(
		code = data['code'],
		product = data['product'],
		price = data['price'],
		discount = data['discount'],
		img = data['img'],
		subcategory = Subcategory.objects.get(name = data['subcategory'])
	).save()
	result = True
	return Response({'result':result})


@api_view(['POST'])
def Get_Category(request):
	category = Category.objects.filter(active = True)
	data = {}
	n = 0
	list_c = []
	for _category in category:
		value = []
		list_c.append({'name':_category.name})
		for i in Subcategory.objects.filter(category = _category):
			value.append({
				"name":i.name,
				"category":_category.name
				})
		data[int(n)] = value
		n+=1
	data['category'] = list_c
	return Response(data)


@api_view(['POST'])
def Get_Product(request):
	run = False
	data = request.data
	subcategory = Subcategory.objects.filter(name = data['subcategory'])
	_data = []
	for i in subcategory:
		for j in Product.objects.filter(subcategory = i):
			_data.append({
				'pk':j.pk,
				'code':j.code,
				"product":j.product,
				"price":Thousands_Separator(int(j.price)),
				"discount":int(j.discount),
				"img":"https://apirapimercado.pythonanywhere.com"+j.img.url,
				"Total_Discount": Thousands_Separator(int(j.Total_Discount()))
			})
	return Response(_data)

@api_view(['POST'])
def Get_All_Product(request):
	run = False
	category = Category.objects.filter(active = True)
	list_product = []
	data = {}
	list_subcategory = []
	n = 0
	value = []
	exist = False
	for x in category:
		list_subcategory.append({'name':x.name})
		for i in Subcategory.objects.filter(category = x):
			for j in Product.objects.filter(subcategory = i)[:5]:
				if j:
					value.append({
						"code": j.code,
						"product": j.product,
						"price":j.price,
						"category":j.subcategory.category.name,
						'subcategory':j.subcategory.name,
						"img":"https://apirapimercado.pythonanywhere.com"+j.img.url
					})
					exist = True
					print(i)
				else:
					exist = False
					print('No existo')

	data['products'] = value
	data['category'] = list_subcategory
	return Response(data)



@api_view(['POST'])
def Get_Product_Only(request):
	try:
		p = Product.objects.get(code = request.data['code'])
		return Response({
			"code":p.code,
			"product":p.product,
			"discount":p.discount,
			"price":p.price,
			"img":"https://apirapimercado.pythonanywhere.com"+p.img.url,
		})
	except Product.DoesNotExist as e:
		return Response({'result':str(e)})
























