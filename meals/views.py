from django.shortcuts import render
from .models import Meals, Category

# Displays list of all meals and categories
def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()

    # Connect variables for the views to the template
    context = {
        'meal_list' : meal_list,
        'categories' : categories,
    }


    # Render to html
    return render(request, 'Meals/list.html', context)




# Displays details of a meal using slug url
def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    # Connect variables for the views to the template
    context = {'meal_detail' : meal_detail}

    # Render to html
    return render(request, 'Meals/detail.html', context)