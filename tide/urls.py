from django.urls import path
from . import views

urlpatterns = [
    path('', views.tide_view, name='tide_view'),
]