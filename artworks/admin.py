from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from .models import ArtWork, ArtWorkImage, ArtWorkTag

@admin.register(ArtWork)
class ArtWorkAdmin(admin.ModelAdmin):
    model = ArtWork
    readonly_fields = ('date_created',)

    list_display = ('title', 'description', 'is_free', 'price')

    fieldsets = (
        ( None, {
            'fields': ('owner','title', 'description')
        }),
        (_('Price'), {
            'fields': ('is_free', 'price',)
        }),
        (_('dates'), {
            'fields': ('date_created',)
        }),
    )

admin.site.register(ArtWorkTag)
admin.site.register(ArtWorkImage)
