from django.shortcuts import render


# Create your views here.
def home_tasks(request):
    return render(request, 'gstTasks/home_tasks.html')
