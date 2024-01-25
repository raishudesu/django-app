from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# to register multiple models, store those in an array
admin.site.register([Question, Choice])
