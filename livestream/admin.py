from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Stream

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    model = Stream
    readonly_fields = ('id', 'started_at')

    list_display = ('id', 'key', 'user', 'is_active')
    ordering = ('id',)
    
    fieldsets = (
        ( None, {
            'fields': ('id', 'key','user', 'is_active', 'started_at', 'ended_at')
        }),
    
    )
