from django.contrib import admin
from .models import Post

# Allows the post model to be visible from the python admin page.
admin.site.register(Post)