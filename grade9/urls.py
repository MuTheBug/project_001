from django.urls import path
from . import views
from grade9.admin import myapp_admin_site

urlpatterns = [
    path('9th', views.main, name="9th"),
    path('9th-admin/', myapp_admin_site.urls),
]


