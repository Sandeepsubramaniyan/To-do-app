from django.contrib import admin
from .models import Todo


class TododAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')

admin.site.register(Todo,TododAdmin)