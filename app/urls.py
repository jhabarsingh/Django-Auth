from app import views
from django.urls import path

urlpatterns = [
	path("register/", views.register,name="app-register"),
	path("", views.index, name="index"),
]
