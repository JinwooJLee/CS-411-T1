from django.urls import path

from . import views

urlpatterns = [
    path('weather/', views.forecast, name='weather'),
]