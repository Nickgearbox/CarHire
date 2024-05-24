from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Contact,Bookings,Area
from app.models import CarImage,Area
#emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        query=Contact(name=name,email=email,message=message)
        query.save()
        #Email sends
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        #this is the email for the admin
        email_message=mail.EmailMessage(f'Email from {name}',f'UserEmail:{email}\n\n\n Message:{message}',from_email,['nicolesonmuhalia@gmail.com'],connection=connection)
        connection.send_messages([email_message])
        connection.close()
        email_client=mail.EmailMessage(f'Nicoleson Response','Thanks for reaching us\n\nnicoleson.tech\n0758820022\nnicolesonmuhalia@gmail.com',from_email,[email],connection=connection)
        connection.send_messages([email_message,email_client])
        connection.close()
    image=CarImage.objects.all()
    context={
        "images":image,
        
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


@login_required
def car(request):
    image=CarImage.objects.all()
    context={
        "images":image
    }
    return render(request,'car.html',context)

@login_required
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        query=Contact(name=name,email=email,message=message)
        query.save()
        #Email sends
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        #this is the email for the admin
        email_message=mail.EmailMessage(f'Email from {name}',f'UserEmail:{email}\n\n\n Message:{message}',from_email,['nicolesonmuhalia@gmail.com'],connection=connection)
        connection.send_messages([email_message])
        connection.close()
        email_client=mail.EmailMessage(f'Nicoleson Response','Thanks for reaching us\n\nnicoleson.tech\n0758820022\nnicolesonmuhalia@gmail.com',from_email,[email],connection=connection)
        connection.send_messages([email_message,email_client])
        connection.close()
        
        messages.info(request,"Message deliverd successfuly. We'll get back to you shortly...")
        return redirect('contact')
        
    return render(request,'contact.html')

@login_required
def booking(request,pk):
    image = get_object_or_404(CarImage, pk=pk)
    #image=CarImage.objects.all()
    area=Area.objects.all()
    context={
        "images":image,
        "areas":area,
    }
    
    if request.method=='POST':
        p_location=request.POST.get('p_location')
        num_adult=request.POST.get('num_adult')
        num_children=request.POST.get('num_children')
        car=request.POST.get('car')
        print("Car",car)
        print("p_location",p_location)
        print("num_adult",num_adult)
        print("num_children",num_children)
        data=Bookings(p_location=p_location,num_adult=num_adult,num_children=num_children,car=car)
        data.save()
    return render(request,'booking.html',context)

@login_required
def detail(request):
    return render(request,'detail.html')

def service(request):
    return render(request,'service.html')


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2') 
        if password!=password2:
            messages.warning(request,'password is incorrect')
            return redirect('register')
        try:
            if User.objects.get(username=username):
                messages.info(request,'user is taken')
                return redirect('register')
        except:
            pass 
        try:
            if User.objects.get(email=email):
                messages.info(request,'email is taken')
                return redirect('register')
        except:
            pass 
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,'Credentials are created')
        return redirect('login')
        
    return render(request ,'register.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request,'login success')
            return redirect('home')
        else:
            messages.error(request,'Invalid  credentials')
            return redirect('login')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    messages.info(request,'Logout successful')
    return redirect('home')
