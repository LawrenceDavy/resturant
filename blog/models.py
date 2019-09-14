from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Structure for blog
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/', blank=True, null=True) 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

# Groups blog posts into different types
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    # Fixes blog subscategory spelling error
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name


# Comments model 
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content