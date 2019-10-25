from django.contrib import admin
from .models import PatrolPoint

# Register your models here.

class PatrolPointAdmin(admin.ModelAdmin):
    '''
        Admin View for PatrolPoint
    '''
    list_display = ('patrol', 'id', 'checkpoint')
    

admin.site.register(PatrolPoint, PatrolPointAdmin)