from django.contrib import admin
from .models import Meals

# Register your models here.


# Add meals model to admin site
admin.site.register(Meals)
