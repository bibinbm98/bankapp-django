from django.shortcuts import redirect,render
from .forms import adduserform,loginform,createaccountform
from .models import User,Account,Login
# Create your views here.


def adduserview(request):
    form=adduserform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=adduserform(request.POST)
        if form.is_valid():
            fname=form.cleaned_data.get("firstname")
            lname=form.cleaned_data.get("lastname")
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            confirmpassword=form.cleaned_data.get("confirmpassword")
            username=form.cleaned_data.get("username")

            user=User(firstname=fname,
                      lastname=lname,
                      email=email,
                      password=password,
                      username=username)
            user.save()
            return redirect("login")
        else:
            context["form"]=form
            return render(request, "bankapp/adduser.html", context)
    return render(request,"bankapp/adduser.html",context)


def login(request):
    form=loginform()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            user = User(password=password,
                        username=username)
            user.save()
            return redirect("login")
        else:
            context["form"] = form
            return render(request, "bankapp/login.html", context)
    return render(request,"bankapp/login.html",context)

        
def account_create(request):
    form=createaccountform()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = createaccountform(request.POST)
        if form.is_valid():
            accountnumber = form.cleaned_data.get("accountnumber")
            accounttype = form.cleaned_data.get("actype")
            username = form.cleaned_data.get("username")
            amount = form.cleaned_data.get("amount")
            print(accountnumber,accounttype,username,amount)
            user = Account(accountnumber=accountnumber,
                        accounttype=accounttype,
                        amount=amount,
                        username=username)
            user.save()
        else:
            context["form"]=form
            return render(request, "bankapp/createaccount.html", context)
    return render(request, "bankapp/createaccount.html", context)
