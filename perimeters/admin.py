from django.contrib import admin
from .models import Perimeter

# Register your models here.

class PerimeterAdmin(admin.ModelAdmin):
    '''
        Admin View for Perimeter
    '''
    list_display = ('user', 'name', 'id')

admin.site.register(Perimeter, PerimeterAdmin)
