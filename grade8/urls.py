from django.urls import path
from . import views

urlpatterns = [
    path('8th', views.main, name="8th")
]
