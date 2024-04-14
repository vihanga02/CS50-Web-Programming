from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("<str:name>", views.greeting, name="greeting"),
    path("vihanga", views.vihanga, name="vihanga")
]