from django.shortcuts import render, redirect
from datetime import datetime
# from home.models import Contact
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# -------------------------------------------------
# -------------------------------------------------
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About.html')

def admit(request):
    return render(request, 'admission.html')
    
def faculty(request):
    return render(request, 'faculty.html')

def event(request):
    return render(request, 'event.html')

# def contact(request):
#     if request.method == "POST":
#         fst_name = request.POST.get('f-name')
#         lst_name = request.POST.get('l-name')
#         email = request.POST.get('email')
#         std_id = request.POST.get('stdid')
#         camp = request.POST.get('Campus')
#         p_code = request.POST.get('p-code')
#         mesg = request.POST.get('msg')
#         CONTACT = Contact(fst_name = fst_name, lst_name = lst_name, email = email, std_id = std_id, 
#         camp = camp, p_code = p_code, mesg = mesg, date = datetime.today())
#         CONTACT.save()
#         messages.success(request, 'Your Form Has Been Submitted')
#     return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

