from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='playground_home'),
        path('add/', views.add_playground, name='add_playground'),
        path('table/', views.playground_table, name='playground_table'),
        path('download/', views.download_phn, name='download_phn'),
        path('all/', views.all_data_table, name='all_data_table'),
        path('tracker/', views.tracker_dashboard, name='tracker_dashboard'),
        path('admin/', views.admin_menu, name='admin_menu'),
        path('admin-login/', views.admin_login, name='admin_login'),
    ]