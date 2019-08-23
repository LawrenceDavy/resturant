# Connect to main url in project folder
from django.urls import path
from . import views

# Django server wants a app name
# Don't know why but this works
app_name = 'reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
   
]