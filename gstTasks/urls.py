from django.urls import path

from gstTasks.views import home_tasks

urlpatterns = [
    path('gestion-taches/', home_tasks, name="home_tasks"),
]
