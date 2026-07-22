from django.contrib import admin
from .models import Todolist
# Register your models here.

class TodolistAdmin(admin.ModelAdmin):
    list_display=("title","description","status")
    search_fields=('id','title')
    list_filter=['status']
    list_per_page=10 
admin.site.register(Todolist,TodolistAdmin)