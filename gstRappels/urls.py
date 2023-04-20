from django.urls import path

from gstRappels.views import CalendarView, appointments, calendrier

urlpatterns = [
    path('gestion-rdv/', CalendarView.as_view(), name="calendar"),
    path('appointments/', appointments, name='appointments'),
    path('calendrier/', calendrier, name='calendrier')
]