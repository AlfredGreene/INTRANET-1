from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    fields = ('author','name','title','description','document')
    list_display = ('author','name','title','description','document')
