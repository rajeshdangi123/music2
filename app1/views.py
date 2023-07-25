from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models.user import Signup,Songs
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    return render(request, "app1/base.html")


def singup1(request):
    if request.method == "GET":
        return render(request, "app1/signup.html")
    else:
        messages.success(request, "welcome to contact")
        postdata = request.POST
        username = postdata.get("user_name")
        first_name = postdata.get("first_name")
        last_name = postdata.get("last_name")
        email = postdata.get("email_field")
        phone_number = postdata.get("phone_number")
        password1 = postdata.get("password1")
        password2 = postdata.get("password2")
        # password=make_password(password1)
        print(username, first_name, last_name, email, password1)

        my_user = Signup(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password1=password1,
            password2=password2,
        )

        if len(username) < 4:
            return render(request, "app1/signup.html")
        elif not first_name:
            return render(request, "app1/signup.html")
        elif my_user.isExists():
            return HttpResponse("email alredy register ")
        elif password1 != password2:
            return render(request, "app1/signup.html")
        else:
            my_user.password1 = make_password(my_user.password1)
            my_user.register()
            return render(request, "app1/login.html")
    return render(request, "app1/signup.html")


def login1(request):
    if request.method == "GET":
        return render(request, "app1/login.html")
    else:
        postdata = request.POST
        email = postdata.get("email_field")
        password1 = postdata.get("password1")

        print("hello1", email, password1)

        customer = Signup.get_customer_by_email(email)
        print("hello2", customer)

        if customer:
            flag = check_password(password1, customer.password1)
            print("hello3", flag)
            if flag:
                request.session["customer"] = customer.id
                # request.session['email_field']=customer.email_field
                print("hello4")

                return redirect("home")
                print("hello")
            else:
                return HttpResponse("Email or Password invalid !!")

        print(email, password1)
        return render(request, "app1/login.html")

    return render(request, "app1/login.html")


def log_out(request):
    request.session.clear()
    return redirect("login1")

    return render(request, "app1/base.html")


def read(request):
    pi= Songs.objects.all()
    return render(request, "app1/read.html",{"pi":pi})

def upload(request):
    if request.method == "POST":
    
        
        song1=request.FILES['song1']
        
    
    
        my_user=Songs(song=song1)
    
        my_user.save()
        return redirect('read')
        
    return render(request, "app1/upload.html")
    


# Create your views here.
