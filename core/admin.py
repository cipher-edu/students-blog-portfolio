from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
class PastAdmin(admin.ModelAdmin):
    list_display = ( 'category', 'title', 'content', 'display_image', 'date',)
    list_filter = ('date',)
   # list_editable = ('title', 'content',  'date',)
    #list_display_links = ('title',)
    list_select_related= ('category',)
    list_per_page = (1)
    def display_image(self, objectcha):
        return mark_safe(f"<img src='{objectcha.image.url}' width='150' height='150' /> ")
admin.site.register(Category)
admin.site.register(Post, PastAdmin)