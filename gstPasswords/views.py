import secrets

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from gstPasswords.models import GenPass


# Create your views here.
@login_required
def home_passwords(request):
    context = {}

    if request.method == "POST":
        site = (request.POST.get('site') or "").strip()
        try:
            password_length = int(request.POST.get('length', 0))
        except (TypeError, ValueError):
            password_length = 0

        if not site:
            context["message"] = "Veuillez saisir un nom de site avant de générer un mot de passe."
        elif password_length < 1:
            context["message"] = "Veuillez sélectionner une longueur de mot de passe valide."
        elif password_length > 30:
            context["message"] = "Impossible de générer un mot de passe de plus de 30 caractères."
        else:
            characters = "!@#$%^&**()_+"
            numbers = "1234567890"
            small_letters = "qwertyuioplkjhgfdsazxcvbnm"
            upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
            alphabet = characters + numbers + small_letters + upper_case

            passwd = ''.join(secrets.choice(alphabet) for _ in range(password_length))
            GenPass.objects.create(site=site, passwords=passwd, user=request.user)
            context['password'] = passwd

    return render(request, 'generator/home_passwords.html', context)


# function listall
@login_required
def listall(request):
    passwords = GenPass.objects.filter(user=request.user)
    context = {
        'passwords': passwords
    }
    return render(request, 'generator/listall.html', context)


@login_required
def search(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query, user=request.user)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


@login_required
def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id=id, user=request.user)
    obj.delete()
    return redirect('listall')
