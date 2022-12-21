from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.forms import Create_User, Register_Form
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from mainapp.models import  User_Data, Match_Data, Register_Match, Id_Pass,  users_match
import random
import razorpay
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def success(request,mname):
    return register_match(request,mname)


# Create your views here.
def hello(request):     
    return render(request,"mainapp\homepage.html")
def profile(request):
    data=User_Data.objects.get(tuser=request.user.username)
    countmatches=Register_Match.objects.filter(username=request.user.username).count()
    context={
        'user':data,
        'countmatches':countmatches
    }
    return render(request,"mainapp\profile.html",context)
    
def showidpass(request):
    checkregister=Register_Match.objects.filter(username=request.user.username,flag_set="yes").values().order_by('-id')
    data={
        'register':checkregister
    }
    return render(request,"mainapp\idpass.html",data)


def dashboard(request):
    d=[]
    client = razorpay.Client(auth=(os.getenv('rzp_live_dXhjAVRL6pxSZS'), os.getenv('Z5LUAaMku0KkXfLeTWhDIuRN')))
    checkreg=Register_Match.objects.all().filter(username=request.user.username).values()
    for i in checkreg:
        d.append(i['match_name'])
    b=Match_Data.objects.all().order_by('-id')
    context={
        'flag':b,
        'temp':d
    }
    return render(request,"mainapp/dashboard.html",context)

def homedashboard(request):
    d=[]
    b=Match_Data.objects.all().order_by('-id')
    context={
        'flag':b
    }
    return render(request,"mainapp/homedashboard.html",context)

def info(request,mname):
    if request.method == "POST":
        data=User_Data.objects.get(tuser=request.user.username)
        p1=request.POST.get("p1")
        p2=request.POST.get("p2")
        p3=request.POST.get("p3")
        p4=request.POST.get("p4")
        p5=p1+"    "+p2+"    "+p3+"    "+p4+"   "+mname
        registerboy=users_match(player_name=p5,mobile_number=data.mobile_number,payment="no")
        registerboy.save()
        return redirect("dashboard")
    return render(request,"mainapp\\regsquad.html")

def register(request):
    flag="success"
    if request.method=="POST":
        username=request.POST.get("tuser")
        print(username)
        email=request.POST.get("email")
        print(email)
        password=request.POST.get("password1")
        print(password)
        try:
            user=User.objects.create_user(username,email,password)
            user.save()
            print(user)
        except:
            flag="fail"
            context={'flag':flag}
            return render(request,"mainapp/register.html",context)
        form2=Register_Form(request.POST)
        if form2.is_valid() :
            form2.save()
            return redirect("login")
        else:
            flag="fail"
    form2=Register_Form()
    context={'form2':form2,'flag':flag}
    return render(request,"mainapp/register.html",context)

def loginpage(request):
    flag="success"
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            flag="fail"
    data={
        'flag':flag
    }
    return render(request,"mainapp/login.html",data)



def register_match(request,mname):
    if request.user.is_authenticated:
        registeruser=Register_Match(username=request.user.username,match_name=mname)
        registeruser.save()
        slotminus=Match_Data.objects.filter(match_name=mname).values()
        print(slotminus)
        slotminus=slotminus[0]
        finalslots=slotminus['slots']-1
        temp=Match_Data.objects.filter(match_name=mname).update(slots=finalslots)
    return redirect("info",mname)

def regmatches(request):
    b=Register_Match.objects.all().filter(username=request.user.username).order_by('-id')
    context={
        'flag':b
    }
    return render(request,"mainapp/regmatch.html",context)

def logoutuser(request):
    logout(request)   
    return redirect('hello')

def about(request):
    return render(request,"mainapp/aboutus.html")

def terms(request):
    return render(request,"mainapp/terms.html")

def privacy(request):
    return render(request,"mainapp/privacy.html")

def refund(request):
    return render(request,"mainapp/refund.html")

def contactus(request):
    if request.method== "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        msg=request.POST.get("message")
        subject = 'User Contact'
        message ='name=' +name + '   email='+email+'   msg='+msg 
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = ['tushargangurde405@gmail.com']
        try: 
            send_mail( subject, message, email_from, recipient_list )
            return redirect('hello')
        except:
            return HttpResponse("unsuccessful") 
    return render(request,"mainapp/contactus.html")