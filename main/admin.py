from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.FormHeader)
admin.site.register(models.FormField)
admin.site.register(models.FormFieldOption)
admin.site.register(models.FormFieldsInOption)


