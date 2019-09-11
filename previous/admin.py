from django.contrib import admin

# Register your models here.
from .models import Previous

class PreviousAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'job')

admin.site.register(Previous, PreviousAdmin)