from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View


# Create your views here.
def signup(request):
    if request.method == "POST":      
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'shop/signup.html')
        
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email is already Taken")
                return render(request,'shop/signup.html')
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        messages.success(request,"Sign-Up Activated Succesfully")
        return redirect('/shopapp/login')

    return render(request,'shop/signup.html')



def login1(request):
    if request.method == "POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'index.html')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/shopapp/login')
    return render(request,'shop/login.html')

def hlogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/shopapp/login')

class RequestResetEmailView(View):
    def get(self,request):
        return render(request,'shop/request-reset-email.html')
    def post(self,request):
        email=request.POST['email']
        user=User.objects.filter(email=email)
        if user.exists():
            email_subjects='[Reset your Password]'
            
            password = request.POST['pass1']
            confirm_password = request.POST['pass2']
            if password != confirm_password:
                messages.warning(request,"Password is Not Matching")
                return render(request,'shop/request-reset-email.html')
        try:
            user=User.objects.get(email=email)
            user.set_password(password)
            user.save()
            messages.success(request,"Password Reset Success Please Login with the New Password")
            return redirect('/shopapp/login/')
        except:
            messages.error(request,"Something went wrong")
            return render(request,'shop/request-reset-email.html')
        

        
    