from django.contrib import admin

from gstDocuments.models import Documents, MotsCles, Tags

# Register your models here.
admin.site.register(Documents)
admin.site.register(MotsCles)

admin.site.register(Tags)

