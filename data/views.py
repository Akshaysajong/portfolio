from django.shortcuts import render, redirect
from .models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def home(request):
    projects = Portfolio.objects.all()[:4]
    tech = TechStack.objects.all()[:4]
    context = {
        "projects":projects,
        "tech" : tech
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    queryset = Portfolio.objects.all()[:4]
    context = {
        "projects":queryset
    }
    return render(request, 'projects.html', context)


def send_email(request):
    if request.method == 'POST':

        template = render_to_string('email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['akshaysekher98@gmail.com']
        )
        email.Fail_silently=False
        email.send()

    return redirect('home')