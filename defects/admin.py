from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import (
    NameAsuModel,
    NumberCabinetModel,
    ModuleTypeModel,
    NumberModuleModel,
    NumberCannelModel,
    ModuleTypeMkcModel,
    NumberCannelMkcModel,
    Journal,
)

# Register your models here.

admin.site.register(Journal)
admin.site.register(NameAsuModel)
admin.site.register(NumberCabinetModel)
admin.site.register(ModuleTypeModel)
admin.site.register(NumberModuleModel)
admin.site.register(NumberCannelModel)
admin.site.register(ModuleTypeMkcModel)
admin.site.register(NumberCannelMkcModel)
