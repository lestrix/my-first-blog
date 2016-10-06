from django.contrib import admin
from .models import Post

# Register your models here.

# import the prveiously created Post model in admin.py 
# to show in admin panel for edit/delete/add

admin.site.register(Post)
