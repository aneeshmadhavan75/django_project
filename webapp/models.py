from django.db import models

# Create your models here.

class signupdb(models.Model):
    Name=models.CharField(max_length=100, null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.CharField(max_length=100, null=True,blank=True)
    Password=models.CharField(max_length=100, null=True,blank=True)
    Confirm_P=models.CharField(max_length=100, null=True,blank=True)
    Profile_img=models.ImageField(upload_to="profile",null=True,blank=True)

class cartdb(models.Model):
    Username=models.CharField(max_length=100, null=True,blank=True)
    Productname=models.CharField(max_length=100, null=True,blank=True)
    Description=models.CharField(max_length=100, null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)

class checkoutdb(models.Model):
    First=models.CharField(max_length=100, null=True,blank=True)
    Last=models.CharField(max_length=100, null=True,blank=True)
    Address=models.CharField(max_length=1000, null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Country=models.CharField(max_length=100, null=True,blank=True)
    State=models.CharField(max_length=100, null=True,blank=True)
    Zip=models.IntegerField(null=True,blank=True)

