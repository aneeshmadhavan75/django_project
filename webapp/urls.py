from django.urls import path
from webapp import views

urlpatterns=[
    path('homepage/', views.homepage,name="homepage"),
    path('aboutpage/', views.aboutpage,name="aboutpage"),
    path('contactpage/', views.contactpage,name="contactpage"),
    path('productpage/<dissp>/', views.productpage,name="productpage"),
    path('singleproduct/<proid>/', views.singleproduct,name="singleproduct"),
    path('registrationpage/', views.registrationpage,name="registrationpage"),
    path('signupsave/', views.signupsave,name="signupsave"),
    path('login/', views.login,name="login"),
    path('logoutsession/', views.logoutsession,name="logoutsession"),
    path('contactsave/', views.contactsave,name="contactsave"),
    path('cartpage/', views.cartpage,name="cartpage"),
    path('cartdetails/', views.cartdetails,name="cartdetails"),
    path('delcart/<int:cartid>', views.delcart,name="delcart"),
    path('checkoutpage/', views.checkoutpage,name="checkoutpage"),
    path('billingsave/', views.billingsave,name="billingsave"),






]