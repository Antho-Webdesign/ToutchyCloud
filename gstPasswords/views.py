from django.shortcuts import render

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