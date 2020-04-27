from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fst-name']
        last_name = request.POST['lst-name']
        username = request.POST['username']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('Done')
        # return redirect('/')
    else:
        return render(request, 'createAcc.html')