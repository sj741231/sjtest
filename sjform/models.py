from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    pubisher = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.title
    
