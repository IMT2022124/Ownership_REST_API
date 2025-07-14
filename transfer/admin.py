from django.contrib import admin
from .models import File, TransferHistory


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'original_owner', 'created_at']

@admin.register(TransferHistory)
class TransferHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'from_user', 'to_user', 'action', 'timestamp']
