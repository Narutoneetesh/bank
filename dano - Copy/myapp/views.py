from django.shortcuts import render,HttpResponse
from .forms import login,signup
from .models import Users


def index(request):
    return render(request, 'myapp/home.html')


def home(request):
    return render(request, 'myapp/home.html')


def Login(request) :
    form = login()
    '''if form.is_valid():
        name = form.cleaned_data['Username']
        password = form.cleaned_data['Password']
        return render(request,'myapp/login.html',)
    else :
        return HttpResponse("<h1>Form is not valid</h1>")'''

    return render(request, 'myapp/login.html',{ 'form':form, })

def Signup(request):
    form = signup()
    return render(request, 'myapp/signup.html',{ 'form':form, })


def contact(request):
    return render(request, 'myapp/contact.html')

def loginsuccess(request):
    form = login(request.POST)
    if form.is_valid():
        name = form.cleaned_data['Username']
        password = form.cleaned_data['Password']
        try :
            user = Users.objects.get(Username=name)
            if password == user.Password :
                request.session['user'] = name
                request.session['password'] = password
                return render(request,'myapp/loginsuccess.html',{'name':name,'password':password})
            else :
                form = login()
                error = "Invalid Password Try Again"
                return render(request,'myapp/home.html',{'form':form,'error':error})

        except Exception as e :
            form = signup()
            return render(request,'myapp/signup.html',{'form':form,'error':"No such user Exist \n Please Signup"})


    else :
        return HttpResponse("<h1>Form is not valid</h1>")

def mksignup(request):
    form = signup(request.POST)
    if form.is_valid():
        Confirm_password = form.cleaned_data['Confirm_Password']
        Password = form.cleaned_data['Password']
        if Password == Confirm_password:
            data = {
            'Username' : form.cleaned_data['Username'],
            'Password' : Password,
            'First_Name' : form.cleaned_data['First_Name'],
            'Last_Name' : form.cleaned_data['Last_Name'],
            'Email'  : form.cleaned_data['Email'],
            'Address'   :form.cleaned_data['Address'],

            }
            obj = Users.objects.create(**data)
            obj.save()
            return render(request,'myapp/signupdone.html',{ 'data':data })

        else:
            return render(request,'myapp/signup.html',{'error':'Password not same'})


    else :
        return HttpResponse("<h1>Form is not valid</h1>")

