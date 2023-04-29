from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Category/$',Create_Category,name="Create_Category"),
	url(r'^Create_SubCategory/$',Create_SubCategory,name="Create_SubCategory"),
	url(r'^Create_Product/$',Create_Product,name="Create_Product"),
	url(r'^Get_Category/$',Get_Category,name="Get_Category"),
	url(r'^Get_Product/$',Get_Product,name="Get_Product"),
	url(r'^Get_All_Product/$',Get_All_Product,name="Get_All_Product"),
	url(r'^Get_Product_Only/$',Get_Product_Only,name="Get_Product_Only"),
]