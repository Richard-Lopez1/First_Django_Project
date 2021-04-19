# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('edit/<int:number>', views.edit),
    path('destroy/<int:number>', views.destroy),
]