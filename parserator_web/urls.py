from django.urls import path

from parserator_web import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/address-parse/', views.AddressParse.as_view(), name='address-parse')
]   # updated path to /address-parse from /parse
