from django.urls import path
from . import views

#url configration
urlpatterns=[
    #path('hello/',views.say_hello)
    path('',views.index, name='home'),
    path('index',views.index, name='index'),
    path('about',views.about, name='about'),
    path('Signup',views.signup, name='signup'),
    path('users',views.users, name='users'),
    path('login',views.login, name='login'),
    path('delete/<int:sno>',views.delete, name='delete'),
    path('update/<int:sno>',views.update, name='update')
]
