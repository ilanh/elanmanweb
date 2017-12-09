from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(RoleObject)
admin.site.register(LogicalGroupObject)
admin.site.register(ConfigSectionObject)
admin.site.register(RoleTaskObject)
admin.site.register(ApiObject)
admin.site.register(ApiSectionObject)
admin.site.register(ApiSubObject)
admin.site.register(ConfigSubObject)
admin.site.register(RoleTemplateObject)
