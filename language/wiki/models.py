import random
from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    
  
    
    
    def save(self, *args, **kwargs):
        self.name = self.name.replace(' ', '-')
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ', '-')
        super(Page, self).save(*args, **kwargs)
       
    def __str__(self):
        return self.title