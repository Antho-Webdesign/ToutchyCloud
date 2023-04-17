from django.shortcuts import render, redirect

from gstTasks.forms import TaskForm
from gstTasks.models import Task


def home_tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    # vérifier la méthode HTTP
    if request.method == "POST":
        # instancier le formulaire avec les données
        form = TaskForm(request.POST)
        # tester la validité du formulaire
        if form.is_valid():
            # save data
            form.save()
            # rediriger vers l'URL "index"
            return redirect("home_tasks")

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'gstTasks/home_tasks.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "gstTasks/update.html", {"edit_task_form": form})


def delete(request, pk):
	task = Task.objects.get(id=pk)
	if request.method == "POST":
		task.delete()
		return redirect("index")
	return render(request, "gstTasks/delete.html",{"task":task})