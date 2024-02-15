from django.urls import path
from .  import views
from django.views import home

urlpatterns = [
    path('admin/', views.home)
]
