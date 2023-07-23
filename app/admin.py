from django.contrib import admin
from .models import Question,Answer

# Register your models here.
class AdminQuestion(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created_at']