from datetime import datetime, date
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Rdv
    template_name = 'gstRappels/home_rdv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.now().date()  # return today's date if no date is specified


def appointments(request):
    appointments = Appointment.objects.all()
    data = [
        {
            'title': appointment.title,
            'start_time': appointment.start_time.isoformat(),
            'end_time': appointment.end_time.isoformat(),
            'description': appointment.description
        }
        for appointment in appointments
    ]
    return JsonResponse(data, safe=False)


def calendar(request):
    appointments = Appointment.objects.all()
    rdv = Rdv.objects.all()
    events = []
    for event in Rdv.objects.all():
        events.append({
            'title': Rdv.title,
            'start_time': Rdv.start_time,
            'end_time': Rdv.end_time,
        })

    context = {
        'appointment': appointments,
        'rdv': rdv,
        'event': event
    }
    return render(request, 'gstRappels/calendar.html', context)


def events(request):
    events = []
    for event in Rdv.objects.all():
        events.append({
            'title': event.titre,
            'start': event.date.strftime('%Y-%m-%dT%H:%M:%S'),
            'url': reverse('rdv_detail', args=[event.pk])
        })
    return JsonResponse(events, safe=False)


def calendrier(request):
    return render(request, 'gstRappels/appointment.html')


@csrf_exempt
def add_appointment(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Méthode de requête non autorisée.'})
    user = request.user
    title = request.POST.get('title')
    start_time = request.POST.get('start')
    end_time = request.POST.get('end')
    description = request.POST.get('description')
    appointment = Appointment(user=user, title=title, start_time=start_time, end_time=end_time, description=description)
    appointment.save()
    return JsonResponse({'success': True})
