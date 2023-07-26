from django.urls import path
from app2.views import *
app2_name="nothing"


urlpatterns=[
    path("page2/",page2,name="page2"),
    path("page3/",page3,name="page3"),
]