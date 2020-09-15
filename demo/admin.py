from django.contrib import admin

from .models import Folder, Note

# Register your models here.


class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder', 'folder_id', 'title')

    def folder_id(self, obj):
        return obj.folder.id


admin.site.register(Folder, FolderAdmin)
admin.site.register(Note, NoteAdmin)
