from django.contrib import admin
from .models import CheckPoint

# Register your models here.

class CheckPointAdmin(admin.ModelAdmin):
    '''
        Admin View for CheckPoint
    '''
    list_display = ('perimeter', 'id', 'bar_code', 'geo_location', 'floor')
   

admin.site.register(CheckPoint, CheckPointAdmin)