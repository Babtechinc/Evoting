
from django.contrib import admin
from django.urls import path
from Account import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('Register', views.Register, name='Register'),
path('state', views.state, name='selectState'),
]
