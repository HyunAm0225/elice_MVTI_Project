from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Character


@admin.register(Character)
class CharacterAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'count', 'rival', 'partner', 'mvti_type',)
