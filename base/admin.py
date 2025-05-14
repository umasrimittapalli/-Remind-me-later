from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'Reminder_method','is_sent')
    list_filter = ('date', 'Reminder_method', 'is_sent')
    search_fields = ('message',)
    readonly_fields = ('created_at', 'updated_at', 'sent_at')
    fieldsets = (
        ('Reminder Details', {
            'fields': ('date', 'time', 'message')
        }),
        ('Delivery Information', {
            'fields': ('Reminder_method',)
        }),
        ('Status Information', {
            'fields': ('is_sent', 'sent_at', 'created_at', 'updated_at')
        }),
    ) 