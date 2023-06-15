from django.shortcuts import render,redirect
from WallApp.models import categorydb,productdb,feedbackdb
from webapp.models import signupdb,cartdb,checkoutdb
from django.contrib import messages
# Create your views here.

def homepage(req):
    cat=categorydb.objects.all()
    pro=productdb.objects.all()
    return render(req, "home.html",{'cat':cat,'pro':pro})

def aboutpage(req):
    cat=categorydb.objects.all()
    return render(req, "about.html",{'cat':cat}) 

def contactpage(req):
    cat=categorydb.objects.all()
    return render(req, "contact.html",{'cat':cat})  

def productpage(req,dissp):
    pro=productdb.objects.filter(Categoryname=dissp)
    cat=categorydb.objects.all()
    return render(req, "product.html",{'pro':pro,'cat':cat}) 

def singleproduct(req, proid):
    pro_s=productdb.objects.get(id=proid)
    cat=categorydb.objects.all()
    return render(req, "singleproduct.html", {'pro_s':pro_s,'cat':cat})

def registrationpage(req):
    return render(req, "registration.html")

def signupsave(req):
    if req.method=="POST":
        nm=req.POST.get('name')
        mb=req.POST.get('mobile')
        em=req.POST.get('email')
        pw=req.POST.get('password')
        pwc=req.POST.get('cpassword')
        img=req.FILES['proimage']
        obj=signupdb(Name=nm, Mobile=mb, Email=em, Password=pw, Confirm_P=pwc, Profile_img=img)
        obj.save()
        messages.success(req, "Sign up Success")
        return redirect(registrationpage)

def login(req):
    if req.method=="POST":
        nm=req.POST.get('name')
        pw=req.POST.get('password')
        if signupdb.objects.filter(Name=nm, Password=pw).exists():
            req.session['Name']=nm
            req.session['Password']=pw
            messages.success(req, "Hurray!!🥳🥳")
            return redirect(homepage)
        else:
            messages.error(req,"Sorry Mate, try again ☠☠")
            return redirect(registrationpage)
      
    messages.error(req,"Sorry Mate, try again ☠☠")
    return redirect(registrationpage)

def logoutsession(req):
    del req.session['Name']
    del req.session['Password']
    return redirect(registrationpage)

def contactsave(req):
    if req.method=="POST":
        nm=req.POST.get('name')
        em=req.POST.get('email')
        ms=req.POST.get('message')
        obj=feedbackdb(Name=nm, Email=em, Message=ms)
        obj.save()
        return redirect(contactpage)

def cartpage(req):
    detail=cartdb.objects.filter(Username=req.session['Name'])
    cat=categorydb.objects.all()
    return render(req, "cart.html",{'detail':detail,'cat':cat})


def cartdetails(req):
    if req.method=="POST":
        nm=req.POST.get('username')
        prd=req.POST.get('proname')
        des=req.POST.get('description')
        prc=req.POST.get('price')
        qnty=req.POST.get('qty')
        obj=cartdb(Username=nm,Productname=prd,Description=des,Price=prc,Quantity=qnty)
        obj.save()
        return redirect(cartpage)


def delcart(req, cartid):
    item=cartdb.objects.filter(id=cartid)
    item.delete()
    return redirect(cartpage)

def checkoutpage(req):
    return render(req, "checkout.html")


def billingsave(req):
    if req.method=="POST":
        fr=req.POST.get('firstname')
        ls=req.POST.get('lastname')
        addr=req.POST.get('address')
        mb=req.POST.get('mobile')
        cnt=req.POST.get('country')
        stt=req.POST.get('state')
        zp=req.POST.get('zipcode')
        obj=checkoutdb(First=fr,Last=ls,Address=addr,Mobile=mb,Country=cnt,State=stt,Zip=zp)
        obj.save()
        messages.success(req, "Your order is confirmed!")
        return redirect(cartpage)
