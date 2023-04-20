from datetime import datetime, date

from django.http import JsonResponse
from django.shortcuts import render
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
    return datetime


def appointments(request):
    appointments = Appointment.objects.all()
    data = [
        {
            'title': Appointment.title,
            'start_time': appointment.start_time.isoformat(Appointment.start_time),
            'end_time': appointment.end_time.isoformat(Appointment.end_time),
            'description': appointment.description
        }
        for appointment in appointments
    ]
    return JsonResponse(data, safe=False)


def calendar(request):
    return render(request, 'gstRappels/calendar.html')


def calendrier(request):
    return render(request, 'gstRappels/appointement.html')


@csrf_exempt
def add_appointment(request):
    if request.method != 'POST':
        # renvoyez une réponse JSON pour indiquer que la méthode de requête n'est pas autorisée
        return JsonResponse({'success': False, 'message': 'Méthode de requête non autorisée.'})
    # récupérez les données de la requête POST
    user = request.user
    title = request.POST.get('title')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    description = request.POST.get('description')
    # créez un nouvel objet Appointment avec les données
    appointment = Appointment(user=user, title=title, start_time=start_time, end_time=end_time, description=description)
    # sauvegardez le rendez-vous dans la base de données
    appointment.save()
    # renvoyez une réponse JSON pour indiquer que le rendez-vous a été ajouté avec succès
    return JsonResponse({'success': True})

