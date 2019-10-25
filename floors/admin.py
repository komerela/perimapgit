from django.contrib import admin
from .models import Floor

# Register your models here.

class FloorAdmin(admin.ModelAdmin):
    '''
        Admin View for Floors
    '''
    list_display = ('name', 'id', 'perimeter')
    

admin.site.register(Floor, FloorAdmin)