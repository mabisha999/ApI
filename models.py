from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length = 200)
    rollNumber = models.CharField(max_length = 200)
    mark = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    caption = models.TextField()
 
    def __str__(self):
        return self.title
class News(models.Model):
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
class Image(models.Model):
    url = models.CharField(max_length=200)   
    def __str__(self):
        return self.url