from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='playground_home'),
    path('add/', views.add_playground, name='add_playground'),
]