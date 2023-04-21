from django.contrib import admin

from gstRappels.models import Rdv, Appointment


class Rdvadmin(admin.ModelAdmin):
    list_display = ('title', 'start_time')


# Register your models here.
admin.site.register(Rdv, Rdvadmin)
admin.site.register(Appointment)
