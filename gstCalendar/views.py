from django.shortcuts import render
import calendar
from calendar import  HTMLCalendar


def home_calendar(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = month_number

    cal = HTMLCalendar().formatmonth(year, month_number)
    context = {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
    }
    return render(request, 'gstCalendar/home_calendar.html', context)
