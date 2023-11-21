from django.urls import path
from . import views as views

urlpatterns = [
    path('login/', name = "login"),
    path('signup/', name = "signup")
]