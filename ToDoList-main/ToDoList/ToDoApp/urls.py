from turtle import update
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.readtask),
    path('create/',views.addtask,name='create'),
    path('update/<title>',views.updatetask),
    path('delete/<title>',views.deletetask),
    path('login',views.loginPage,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logoutUser,name='logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    
