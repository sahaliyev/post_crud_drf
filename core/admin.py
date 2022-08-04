from django.contrib import admin

# Register your models here.
from .models import News, Comments


admin.site.register(News)
admin.site.register(Comments)