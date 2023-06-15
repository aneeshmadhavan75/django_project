from django.urls import path
from WallApp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('categorysave/',views.categorysave,name="categorysave"),
    path('category_display/',views.category_display,name="category_display"),
    path('category_edit/<int:dataid>/',views.category_edit,name="category_edit"),
    path('category_update/<int:dataid>/',views.category_update,name="category_update"),
    path('category_del/<int:dataid>/',views.category_del,name="category_del"),
    path('addproductpage/',views.addproductpage,name="addproductpage"),
    path('productsave/',views.productsave,name="productsave"),
    path('product_display/',views.product_display,name="product_display"),
    path('product_edit/<int:dataid>/',views.product_edit,name="product_edit"),
    path('product_update/<int:dataid>/',views.product_update,name="product_update"),
    path('product_del/<int:dataid>/',views.product_del,name="product_del"),
    path('',views.loginpage,name="loginpage"),
    path('adminverify/',views.adminverify,name="adminverify"),
    path('deletesession/',views.deletesession,name="deletesession"),
    path('feeddisplay/',views.feeddisplay,name="feeddisplay"),
    path('delfeed/<int:feedid>/',views.delfeed,name="delfeed"),
    



]
