from django.urls import path
from django.contrib import admin
from . import views

app_name='manager' 

urlpatterns = [    
    path('', views.manager_index, name="home"),
	path('menu/', views.menu_list, name="menu_list"),
	path('menu_add/', views.menu_add, name="menu_add"),
	path('add_menu_data/', views.add_menu_data, name="add_menu_data"),
	path('detail/<int:menu_id>', views.menu_detail, name="menu_detail"),
	path('add_option/<int:menu_id>', views.add_option, name="add_option"),
	path('add_option_data', views.add_option_data, name="add_option_data"),
	
]	