from django.contrib import admin 
  
# Register your models here. 
from .models import Product,Student,Post,News,Image
  
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(News)
admin.site.register(Image)
