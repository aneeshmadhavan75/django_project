from django.db import models

# Create your models here.

class categorydb(models.Model):
    Categoryname=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=1000,null=True,blank=True)
    Image=models.ImageField(upload_to="categ_pic",null=True,blank=True)

class productdb(models.Model):
    Categoryname=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Brandname=models.CharField(max_length=100,null=True,blank=True)
    Price=models.CharField(max_length=100,null=True,blank=True)
    Pro_description=models.CharField(max_length=1000,null=True,blank=True)
    Pro_image=models.ImageField(upload_to="product_img",null=True,blank=True)

class feedbackdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=5000,null=True,blank=True)
