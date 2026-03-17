from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class BaseModel(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class NameAsuModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class NumberCabinetModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class ModuleTypeModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class NumberModuleModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class NumberCannelModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class ModuleTypeMkcModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class NumberCannelMkcModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    

class Journal(models.Model):
    date_def = models.DateField(null=True, verbose_name='Дата неисправности')
    name_asu = models.ForeignKey(NameAsuModel, on_delete=models.CASCADE, verbose_name='Наименование АСУ ТП')
    number_cabinet = models.ForeignKey(NumberCabinetModel, on_delete=models.CASCADE, verbose_name='№ шкафа ПТК')
    module_type = models.ForeignKey(ModuleTypeModel, on_delete=models.CASCADE, verbose_name='Тип модуля УСО')
    number_module = models.ForeignKey(NumberModuleModel, on_delete=models.CASCADE, verbose_name='№ модуля УСО')
    number_cannel = models.ForeignKey(NumberCannelModel, on_delete=models.CASCADE, verbose_name='№ канала УСО')
    module_type_mkc = models.ForeignKey(ModuleTypeMkcModel, on_delete=models.CASCADE, verbose_name='Тип модуля МКС')
    number_module_mkc =  models.CharField(max_length=255, verbose_name='№ модуля МКС')
    number_cannel_mkc = models.ForeignKey(NumberCannelMkcModel, on_delete=models.CASCADE, verbose_name='№ канала МКС')
    channel_purpose = models.CharField(max_length=255, verbose_name='Назначение канала')
    fault = models.CharField(max_length=255, verbose_name='Неисправность')
    author_def = models.CharField(max_length=255, verbose_name='Автор записи')
    events = models.CharField(max_length=255, verbose_name='Мероприятия')
    date_events = models.DateField(null=True, verbose_name='Дата мероприятия')
    author_events = models.CharField(max_length=255, verbose_name='Автор мероприятий')
    events_two = models.CharField(max_length=255, verbose_name='Мероприятия-2')
    date_events_two = models.DateField(null=True, verbose_name='Дата мероприятия-2')
    author_events_two = models.CharField(max_length=255, verbose_name='Автор мероприятий-2')
   
    class Meta:
        ordering = ['-date_events']

    def __str__(self):
        return f'{self.date_def} | {self.fault} | {self.author_def}'

# class JournalEvents(models.Model):
#     events = models.CharField(max_length=255, verbose_name='Мероприятия')
#     date_events = models.DateField(null=True, verbose_name='Дата мероприятия')
#     author_events = models.CharField(max_length=255, verbose_name='Автор мероприятий')

  
