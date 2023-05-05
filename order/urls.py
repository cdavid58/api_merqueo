from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Order/$',Create_Order,name="Create_Order"),
	url(r'^Download_Order/$',Download_Order,name="Download_Order"),
	url(r'^Update_State/$',Update_State,name="Update_State"),
]