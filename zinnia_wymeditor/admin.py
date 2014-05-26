"""EntryAdmin for zinnia-wymeditor"""
from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin


class EntryAdminWYMEditorMixin(object):
    """
    Mixin adding WYMeditor for editing Entry.content field.
    """
    pass


class EntryAdminWYMEditor(EntryAdminWYMEditorMixin,
                          EntryAdmin):
    """
    Enrich the default EntryAdmin with WYMEditor.
    """
    pass

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdminWYMEditor)
