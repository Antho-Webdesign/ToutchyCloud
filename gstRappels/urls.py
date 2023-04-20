from django.urls import path

from gstRappels.views import CalendarView, appointments, calendrier, calendar, add_appointment

urlpatterns = [
    path('gestion-rdv/', CalendarView.as_view(), name="calendar"),
    path('appointments/', appointments, name='appointments'),
    path('calendrier/', calendrier, name='calendrier'),
    path('calendar/', calendar, name='calendar'),
    path('add_appointment/', add_appointment, name='add_appointment'),
]