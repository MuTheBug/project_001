from django.urls import path
from . import views

urlpatterns = [
    path('7th', views.main, name="7th")
]
