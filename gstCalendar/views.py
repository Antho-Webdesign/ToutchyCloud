from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import calendar
from calendar import HTMLCalendar

from django.urls import reverse

from gstCalendar.models import Event


def home_calendar(request, year, month):
    events = Event.objects.all()
    # events = get_object_or_404(Event)
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = month_number

    cal = HTMLCalendar().formatmonth(year, month_number)


    context = {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'events': events,
    }
    return render(request, 'gstCalendar/home_calendar.html', context)


def add_event(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Méthode de requête non autorisée.'})
    user = request.user
    title = request.POST.get('title')
    start_time = request.POST.get('start')
    end_time = request.POST.get('end')
    description = request.POST.get('description')
    appointment = Event(user=user, title=title, start_time=start_time, end_time=end_time, description=description)
    appointment.save()
    return JsonResponse({'success': True})
