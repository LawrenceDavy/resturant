# Connect to main url in project folder
from django.urls import path
from . import views

# Django server wants a app name
# Don't know why but this works
app_name = 'meals'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail')
]