from django.contrib import admin

# Register your models here.
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner', 'date_added')
    list_display_links = ('text',)
    search_fields = ('text', 'owner',)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added')
    list_display_links = ('text',)
    search_fields = ('text',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
