from django.urls import *
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('intro' , views.intro, name='intro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('first' , views.first, name='first'),
    path('second', views.second, name='second'),
    path('quest1', views.quest1, name='quest1'),
    path('quest2', views.quest2, name = 'quest2'),
    path('quest3', views.quest3,name='quest3'),
    path('result', views.result, name='result'),
    path('chathome' ,views.chathome, name='chathome'),
    path('<str:room>/', views.chatroom, name='chatroom'),
    path('checkview', views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('quest4', views.quest4, name='quest4'),
    path('quest5', views.quest5, name='quest5'),
    path('quest6', views.quest6, name='quest6'),
    path('quest7', views.quest7, name='quest7'),
    path('quest8', views.quest8, name='quest8'),
    path('quest9', views.quest9, name='quest9'),
    path('quest10', views.quest10, name='quest10'),
    path('quest11', views.quest11, name='quest11'),
    path('quest12', views.quest12, name='quest12'),
    path('quest13', views.quest13, name='quest13'),
    path('quest14', views.quest14, name='quest14'),
    path('quest15', views.quest15, name='quest15'),
    path('quest16', views.quest16, name='quest16'),
    path('semiresult', views.semiresult, name='semiresult'),



]