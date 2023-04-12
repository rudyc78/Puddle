from django.contrib import admin

# Register your models here.

from .models import Category  ##Adding the ".models" means that the category is under the same folder
# Register your models here.  
from .models import Item

admin.site.register(Category)
admin.site.register(Item)