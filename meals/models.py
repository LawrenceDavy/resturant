from django.db import models
from django.utils.text import slugify



# Structure for meal information
class Meals(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True) # Link meals to category. SET_NULL stops category from getting deleted when deleting a meal
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preperation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            super(Meals, self).save(*args, **kwargs)

    # Fixes meals subscategory spelling error
    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    # name of meal appears in admin
    def __str__(self):
        return self.name




# Structure for food category menu ie. Breakfast, Lunch, Dinner
class Category(models.Model):
    name = models.CharField(max_length=30)

    # # Fixes Category subscategory spelling error
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # Name of category appears in admin
    def __str__(self):
        return self.name

