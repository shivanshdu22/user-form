from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import user


def home(request):
    return render(request, 'home.html')


def submit(request):
    val1 = request.POST['name']
    val2 = request.POST['DOB']
    val3 = request.POST['email_id']
    val4 = request.POST['phone']
    usernew = user(name=val1, dob=val2, email=val3, phone=val4)

    send_mail(
        'Hello!',
        'Welcome New user! Your data is saved. ',
        'Shivansh Dubey',
        [val3],
        fail_silently=False,
    )
    usernew.save()
    return render(request, 'home.html')
