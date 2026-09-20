from django.contrib import admin
from django.utils.html import format_html
from .models import PhotoSession

@admin.register(PhotoSession)
class PhotoSessionAdmin(admin.ModelAdmin):
    # Columns to display in the main list view
    list_display = ('id', 'created_at',
                    'has_composite', 'has_gif')
    
    # Allow filtering by date in the sidebar
    list_filter = ('created_at',)
    
    # Allow searching by the UUID
    search_fields = ('id',)
    
    # Prevent these fields from being edited manually
    readonly_fields = ('id', 'created_at', 'qr_code_preview')

    # Organize the detail view into clean sections
    fieldsets = (
        ('Session Details', {
            'fields': ('id', 'created_at',
                       'qr_code', 'qr_code_preview')
        }),
        ('Raw Photos', {
            'fields': ('photo_1', 'photo_2',
                       'photo_3', 'photo_4')
        }),
        ('Processed Outputs', {
            'fields': ('composite_frame', 'gif_video')
        }),
    )

    # --- Custom Display Methods ---

    def has_composite(self, obj):
        """Shows a nice checkmark/x icon in the list view if the composite is uploaded"""
        return bool(obj.composite_frame)
    has_composite.boolean = True
    has_composite.short_description = 'Composite Ready'

    def has_gif(self, obj):
        """Shows a nice checkmark/x icon in the list view if the GIF is uploaded"""
        return bool(obj.gif_video)
    has_gif.boolean = True
    has_gif.short_description = 'GIF Ready'

    def qr_code_preview(self, obj):
        """Renders the actual QR code image in the admin detail view"""
        if obj.qr_code:
            return format_html(
                '<img src="{}" width="150" height="150" style="border: 1px solid #ccc;" />', 
                obj.qr_code.url
            )
        return "No QR Code generated yet."
    qr_code_preview.short_description = 'QR Code Preview'

