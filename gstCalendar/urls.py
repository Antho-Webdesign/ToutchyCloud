from django.urls import path

from gstCalendar.views import home_calendar

urlpatterns = [
   path('<int:year>/<str:month>/home-calendar/', home_calendar, name='home_calendar')
]