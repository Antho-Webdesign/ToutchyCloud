from django.urls import path

from gstRappels.views import CalendarView

urlpatterns = [
    path('gestion-rdv/', CalendarView.as_view(), name="calendar"),
]