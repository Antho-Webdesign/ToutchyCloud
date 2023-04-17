from django.urls import path

from gstTasks.views import home_tasks, update, delete

urlpatterns = [
    path('gestion-taches/', home_tasks, name="home_tasks"),
    path('update/<slug:slug>/', update, name="update"),
    path('delete/<slug:slug>/', delete, name="delete"),
]
