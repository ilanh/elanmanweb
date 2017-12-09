from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(RoleObject)
admin.site.register(LogicalGroupObject)
admin.site.register(ConfigSectionObject)
admin.site.register(RoleTaskObject)