from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ladning_page, name="landing_page"),
    path('inventory', views.inventory, name="inventory"),
    path("<pk>", views.delete, name="delete")
]
