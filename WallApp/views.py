from django.shortcuts import render,redirect
from WallApp.models import categorydb,productdb,feedbackdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from webapp.views import contactpage
from django.contrib import messages

# Create your views here.

def homepage(req):
    return render(req, "index.html")

def categorypage(req):
    return render(req, "addcategory.html")

def categorysave(req):
    if req.method=="POST":
        cat=req.POST.get('category')
        des=req.POST.get('description')
        catimg=req.FILES['categoryimage']
        obj=categorydb(Categoryname=cat,Description=des,Image=catimg)
        obj.save()
        messages.success(req, "Category added succesfully!!")
        return redirect(categorypage)

def category_display(req):
    data=categorydb.objects.all()
    return render(req, "displaycateg.html",{'data': data})

def category_edit(req, dataid):
    data=categorydb.objects.get(id=dataid)
    return render(req, "editcategory.html", {'data':data})

def category_update(req, dataid):
    if req.method=="POST":
        cat=req.POST.get('category')
        des=req.POST.get('description')
        try:
            catimg=req.FILES['categoryimage']
            fs=FileSystemStorage()
            file=fs.save(catimg.name, catimg)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Categoryname=cat,Description=des,Image=file)
        return redirect(category_display)
    
def category_del(req, dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(category_display)

def addproductpage(req):
    data=categorydb.objects.all()
    return render(req, "addproduct.html", {'data':data})

def productsave(req):
    if req.method=="POST":
        cat=req.POST.get('category')
        prd=req.POST.get('product')
        brd=req.POST.get('brand')
        prc=req.POST.get('price')
        desc=req.POST.get('productdesc')
        pimg=req.FILES['productimage']
        obj=productdb(Categoryname=cat,Productname=prd,Brandname=brd,Price=prc,Pro_description=desc,Pro_image=pimg)
        obj.save()
        return redirect(addproductpage)

def product_display(req):
    data=productdb.objects.all()
    return render(req, "displayprod.html", {'data':data})

def product_edit(req, dataid):
    cat=categorydb.objects.all()
    data=productdb.objects.get(id=dataid)
    return render(req, "editproduct.html", {'data':data,'cat':cat})

def product_update(req, dataid):
    if req.method=="POST":
        cat=req.POST.get('category')
        prd=req.POST.get('product')
        brd=req.POST.get('brand')
        prc=req.POST.get('price')
        desc=req.POST.get('productdesc')
        try:
            pimg=req.FILES['productimage']
            fs=FileSystemStorage()
            file=fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Pro_image
        productdb.objects.filter(id=dataid).update(Categoryname=cat,Productname=prd,Brandname=brd,Price=prc,Pro_description=desc,Pro_image=file)
        return redirect(product_display)
    
def product_del(req, dataid):
    data=productdb.objects.get(id=dataid)
    data.delete()
    return redirect(product_display)

def loginpage(req):
    return render(req,"login.html")

def adminverify(req):
    if req.method=="POST":
        uname=req.POST.get('username')
        pword=req.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            verify=authenticate(username=uname,password=pword)

            if verify is not None:
                login(req, verify)
                req.session['username']=uname
                req.session['password']=pword
                messages.success(req,"Admin login success!")
                return redirect(homepage)
            else:
                messages.error(req, "Invalid credentials!")
                return redirect(loginpage)
        else:
            messages.error(req, "Invalid credentials!")
            return redirect(loginpage)

def deletesession(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)

def feeddisplay(req):
    feed=feedbackdb.objects.all()
    return render(req, "feedback.html", {'feed':feed})

def delfeed(req, feedid):
    msgdel=feedbackdb.objects.filter(id=feedid)
    msgdel.delete()
    return redirect(feeddisplay)
    