from django.urls import path
from app1.views import *
app1_name="something"



urlpatterns=[
    path("page/",page,name="page"),
    path("page1/",page1,name="page1")
]