from django.db import models

# Create your models here.

class Article(models.Model):
  title = models.TextField()
  content =  models.TextField()
  category =  models.TextField()
  author =  models.TextField()
  date_published =  models.TextField()
  date_updated =  models.TextField()

