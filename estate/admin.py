from django.contrib import admin
from django.utils.safestring import mark_safe

from estate.models import *



class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'zipcode', 'slug', 'category', 'get_html_photo')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'zipcode', 'slug', 'category', 'image')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=50>')

    get_html_photo.short_description = 'Miniature'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'slug')





admin.site.register(PropertyModel, PropertyAdmin)
admin.site.register(PropertyCategory, CategoryAdmin)
admin.site.register(Email)
