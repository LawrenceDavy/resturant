from django.contrib import admin
from .models import Meals, Category

# Register your models here.


# Add meals model to admin site
admin.site.register(Meals)

# Add category model to admin site 
admin.site.register(Category)
