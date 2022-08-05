from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_image')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'нет картинки'

    get_image.short_description = 'Миниатюра'


admin.site.register(CmsSlider, CmsAdmin)
