from django.contrib import admin
from .models import *

# Register your models here.


class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name_complete', 'address')
    search_fields = ["name_complete"]


admin.site.register(PersonalInformation)


