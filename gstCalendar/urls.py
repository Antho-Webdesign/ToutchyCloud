from django.urls import path

from gstCalendar.views import home_calendar, add_event

urlpatterns = [
   path('home-calendar/<int:year>/<str:month>/', home_calendar, name='home_calendar'),
   path('add_event/', add_event, name='add_event'),
]