from django.contrib import admin
from .models import Users
from .models import Todo

# Register your models here.
admin.site.register(Users)
admin.site.register(Todo)
