from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('admit', views.admit, name='admit'),
    path('faculty', views.faculty, name='faculty'),
    path('event', views.event, name='event'),
    # path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('creataccount', views.creataccount, name='creataccount'),
]
