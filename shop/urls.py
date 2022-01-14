from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('we/', views.we, name='we'),
    path('catalog/', views.catalog, name='catalog'),
    path('devivery/', views.delivery_pay, name='delivery_pay'),
    path('exchange/', views.exchange_return, name='exchange_return'),
    path('info/', views.info, name='info'),
    path('contacts/', views.contacts, name='contacts'),
    path('item/<int:pk>/', views.flower_item, name='flower_item'),
    path('example/<int:pk>/', views.example, name='example')
]
