from django.shortcuts import render,redirect
from .models import Record
from django.contrib.auth.models import User
from django.core.mail import send_mail
import smtplib 
from kitab_ghar.settings import EMAIL_HOST_USER

# Create your views here.


def home(request):
    if User.is_staff:
        if request.method == 'POST':
            name                    = request.POST["name"]
            email                   = request.POST["email"]
            track                   = request.POST["track"]
            book                    = request.POST["book"]
            pincode                 = request.POST["pincode"]
            village                 = request.POST["village"]
            date                    = request.POST["date"]
            payment                 = request.POST["payment"]
            total                   = request.POST["total"]
            phone                   = request.POST["phone"]

            x = Record.objects.create(
            email=email,
            name=name,
            track=track,
            book=book,
            pincode=pincode,
            village=village,
            date=date,
            payment=payment,
            total=total,
            phone=phone
            )
            x.save()
          

        return render(request,'index.html')
    
    else:
        return render(request,'404.html')

def filter(request):

    if User.is_superuser:
        x = Record.objects.all()

        if request.method == 'POST':
            filter_id          = request.POST["filter_id"]
            value              = request.POST["value"]
            

            if(filter_id == 'email'):
                x = Record.objects.filter(email=value)
            
            if(filter_id == 'name'):
                x = Record.objects.filter(name=value)
            if(filter_id == 'track'):
                x = Record.objects.filter(track=value)
            if(filter_id == 'book'):
                x = Record.objects.filter(book=value)
            if(filter_id == 'pincode'):
                x = Record.objects.filter(pincode=value)
            if(filter_id == 'village'):
                x = Record.objects.filter(village=value)
            if(filter_id == 'date'):
                x = Record.objects.filter(date=value)
            if(filter_id == 'payment'):
                x = Record.objects.filter(payment=value)
            if(filter_id == 'total'):
                x = Record.objects.filter(total=value)
            if(filter_id == 'phone'):
                x = Record.objects.filter(phone=value)

        return render(request,'tables.html',{'x':x})

    else:
        return render(request,'404.html')

def mail(request):
    if User.is_superuser:

        if request.method == "POST":
            recievers = []
            track   =   request.POST["track"]
            email   =   request.POST["email"]
            recievers.append(email)
            send_mail("trackin ID For your Order", "greetings From Kitab Ghar your Track code is      \n  {    "+ track +"     }       you can trace it at https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx", EMAIL_HOST_USER, recievers)

        return render(request,'mail.html')

    else:

        return render(request,'404.html')
