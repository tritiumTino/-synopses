from django.contrib import admin

# Register your models here.
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner', 'date_added')
    list_display_links = ('text',)
    search_fields = ('text', 'owner',)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'title', 'view_text', 'date_added')
    list_display_links = ('title', 'view_text',)
    search_fields = ('title', 'view_text',)

    @admin.display(empty_value='???')
    def view_text(self, obj):
        return obj.text[:80]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
