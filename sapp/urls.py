from django.urls import path
from sapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('purchase',views.purchase,name='purchase'),
    path('home',views.home,name='home'),
]