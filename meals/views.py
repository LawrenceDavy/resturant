from django.shortcuts import render
from .models import Meals

# Displays list of all meals
def meal_list(request):
    meal_list = Meals.objects.all()

    context = {'meal_list' : meal_list}

    return render(request, 'Meals/list.html', context)

# Displays details of meal
def meal_detail(request, slug):
    pass
