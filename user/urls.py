from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_User/$',Create_User,name="Create_User"),
	url(r'^Login/$',Login,name="Login"),
]