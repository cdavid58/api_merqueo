from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Order/$',Create_Order,name="Create_Order"),
]