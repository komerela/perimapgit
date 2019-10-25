from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    '''
        Admin View for CustomUser
    '''
    list_display = ('id', 'email', 'first_name')


admin.site.register(CustomUser, CustomUserAdmin)
