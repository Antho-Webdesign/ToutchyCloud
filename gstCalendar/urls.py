from django.urls import path

from gstCalendar.views import home_calendar, add_event

urlpatterns = [
   path('home-calendar/<int:year>/<str:month>/', home_calendar, name='home_calendar'), # http://127.0.0.1:8000/home-calendar/2023/april/
   path('add_event/', add_event, name='add_event'),
]