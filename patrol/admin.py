from django.contrib import admin
from .models import Patrol

# Register your models here.

class PatrolAdmin(admin.ModelAdmin):
    '''
        Admin View for Patrol
    '''
    list_display = ('time', 'id', 'perimeter')
    

admin.site.register(Patrol, PatrolAdmin)
