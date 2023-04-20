from datetime import datetime, date

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import generic

from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Rdv
    template_name = 'gstRappels/home_rdv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.now()


def appointments(request):
    appointments = Appointment.objects.all()
    data = [
        {
            'title': appointment.title,
            'start': appointment.start_time.isoformat(),
            'end': appointment.end_time.isoformat(),
            'description': appointment.description,
        }
        for appointment in appointments
    ]
    return JsonResponse(data, safe=False)


def calendar(request):
    return render(request, 'gstRappels/calendar.html')

def calendrier(request):
    return render(request, 'gstRappels/appointement.html')