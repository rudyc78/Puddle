from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)


    class Meta: ###This will prevent django from creating the table name misspelled.
        ordering = ('name',) ##This will sort the items by name
        verbose_name_plural ='Categories'


    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name = 'items', on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'item_images', blank = True, null = True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) ###models.CASCADE: if an item is deleted, the data remaining will also be deleted as well
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name