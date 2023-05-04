from django.db import models

# Create your models here.

class Conversation(models.Model):
    item = models.models.ForeignKey(Item, related_name='converations', on_delete=models.CASCADE)