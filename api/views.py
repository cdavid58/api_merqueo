from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Category
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
		name_db = str(request.data['name'])+'.db'
		if not path.isfile(name_db):
			c = sqlite3.connect(name_db)
			c.close()
		result = True
	return Response({'result':result})

def Connection(name):
	return sqlite3.connect(name+'.db')

@api_view(['POST'])
def Create_SubCategory(request):
	data = request.data
	run = False
	try:
		c = Connection(Category.objects.get(name = data['category']).name)
		run = True
	except Exception as e:
		print(e)

	print(data['subcategory'])

	if run:
		cursor = c.cursor()
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS """+str(data['subcategory'])+""" (
			   	code int not null unique,
			   	product char(150) not null,
			   	price decimal(7,1) not null,
			   	discount int not null,
			   	img text null
			);
		""")
		c.commit()

	return Response(True)

@api_view(['POST'])
def Create_Product(request):
	data = request.data
	run = False
	result = False
	try:
		c = Connection(Category.objects.get(name = data['category']).name)
		run = True
	except Exception as e:
		print(e)
	if run:
		cursor = c.cursor()
		query = """
			insert into """+str(data['subcategory'])+"""
			(
				code,product,price,discount
			)
			values(?,?,?,?);
		"""
		args = (
			data['code'],str(data['product']),data['price'],data['discount']
		)
		cursor.execute(query,args)
		c.commit()
		result = True

	return Response({'result':result})


@api_view(['POST'])
def Get_Category(request):
	category = Category.objects.all()
	data = []
	list_sub = []
	for _category in category:
		c = Connection(_category.name)
		cursor = c.cursor()
		cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
		n = 0
		_data = cursor.fetchall()
		list_sub.append(_data[0][1])
	n = 0
	for i in category:
		data.append({
			"category":i.name,
			"subcategory": list_sub[n],
			"url_menu": str(list_sub[n]).replace(' ','_')
		})
		n += 1
	return Response(data)


@api_view(['POST'])
def Get_Product(request):
	run = False
	data = request.data
	try:
		c = Connection(Category.objects.get(name = data['category']).name)
		run = True
	except Exception as e:
		print(e)

	if run:
		cursor = c.cursor()
		cursor.execute("select * from "+str(data['subcategory']))
		data = []
		for i in cursor.fetchall():
			price = float(i[2])
			discount = float(i[3])
			print(discount)
			total_discount = price - (price * (discount / 100))
			print(total_discount)
			data.append(
				{
					'code': i[0],
					'product':i[1],
					'price': Thousands_Separator(i[2]),
					'discount':discount,
					'total_discount': Thousands_Separator(total_discount),
					'img':i[4]
				}
			)
	return Response(data)

@api_view(['POST'])
def Get_All_Product(request):
	run = False
	data = request.data
	category = Category.objects.all()
	list_product = []
	for j in category:
		try:
			c = Connection(j.name)
			run = True
		except Exception as e:
			print(e)
		cursor = c.cursor()
		cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
		n = 0
		_data = cursor.fetchall()
		print(_data[0][1])
		cursor = c.cursor()
		for x in _data:
			cursor.execute("select * from "+str(x[1])+" limit 10")
			list_product.append([
				{
					'code': i[0],
					'product':i[1],
					'price':i[2],
					'discount':i[3],
					'category':j.name,
					'subcategory':_data[0][1]
				}
				for i in cursor.fetchall()
			]
		)
				
	return Response(list_product)




























