from django.urls import path
from . import views

urlpatterns = [
    path('12th', views.main, name="12th")
]
