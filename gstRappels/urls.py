from django.urls import path

from gstRappels.views import CalendarView, appointments, calendrier, calendar

urlpatterns = [
    path('gestion-rdv/', CalendarView.as_view(), name="calendar"),
    path('appointments/', appointments, name='appointments'),
    path('calendrier/', calendrier, name='calendrier'),
    path('calendar/', calendar, name='calendar'),
]