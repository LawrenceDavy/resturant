from django.urls import path
from . import views

# Django server wants a app name
# Don't know why but this works
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail') 
]