from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from adminfiles.admin import FilePickerAdmin

class FlatPageAdmin(FilePickerAdmin):
    adminfiles_fields = ('content',)
    exclude = ('enable_comments', )
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
