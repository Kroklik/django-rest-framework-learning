from django.contrib import admin
from django.shortcuts import render

from .models import Category, Actor
# Register your models here.

admin.site.register(Category)
admin.site.register(Actor)
