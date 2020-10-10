from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login



def register(request):
    if request.method == 'POST':
        first_name  = request.POST["first_name"]
        last_name   = request.POST["last_name"]
        # username    = request.POST["username"]
        password1   = request.POST["password1"]
        password2   = request.POST["password2"]
        email       = request.POST["email"]
        if password1 == password2:

            if User.objects.filter(email=email).exists():

                messages.info(request, 'Email is already taken')

            else :

                user        = User.objects.create_user(username = email,password = password1,email = email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request, "Signup Successful. You are now able to login")
                return redirect('login')
        else:
            print('passwords dont match')
            messages.info(request, "Passwords dont match")
            return redirect('register')




    return render(request,'register.html')

def sign_in(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            
            return redirect('home')
            
        else:
            messages.info(request, 'Invalid Credentials')

            return redirect('login')



    return render(request,'login.html')

        
        
