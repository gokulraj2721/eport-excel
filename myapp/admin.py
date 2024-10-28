from django.contrib import admin
from .models import Details
from django.http import HttpResponse

from import_export.admin import ExportActionMixin

class MyDataAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('name','description','created_at')


admin.site.register (Details, MyDataAdmin)
# Register your models here.
