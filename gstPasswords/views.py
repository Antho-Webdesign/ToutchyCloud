import random

from django.shortcuts import render, get_object_or_404, redirect

from gstPasswords.models import GenPass


# Create your views here.
def home_passwords(request):
    if request.method != "POST":
        return render(request, 'generator/home_passwords.html')
    else:
        site = request.POST.get('site')
        if site == "":
            return render(request, 'generator/home_passwords.html')
        password_length = int(request.POST.get('length'))
        characters = "!@#$%^&**()_+"
        numbers = '1234567890'
        small_letters = "qwertyuioplkjhgfdsazxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
        prep = characters + numbers + small_letters + upper_case
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            context = {
                'message': message
            }
            return render(request, 'generator/home_passwords.html', context)

        else:
            passwd = ''.join(random.sample(prep, k=password_length))
            print(passwd)
            p = GenPass.objects.create(site=site, passwords=passwd, user=request.user)
            p.save()
            context = {
                'password': passwd
            }
            return render(request, 'generator/home_passwords.html', context)


# function listall
def listall(request):
    passwords = GenPass.objects.filter(user=request.user)
    context = {
        'passwords': passwords
    }
    return render(request, 'generator/listall.html', context)


def search(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query, user=request.user)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id=id)
    obj.delete()
    return redirect('listall')


"""

def search(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query, user=request.user)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id=id)
    obj.delete()
    return redirect('listall')


def home_test(request):
    return render(request, 'generator/home-test.html')

"""
