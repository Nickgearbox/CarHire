from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('booking/<int:pk>/',views.booking,name='booking'),
    path('car',views.car,name='car'),
    path('contact',views.contact,name='contact'),
    path('detail',views.detail,name='detail'),
    path('service',views.service,name='service'),
    path('register',views.register,name='register'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logoutuser'),
    
]


