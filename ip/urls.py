from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name ='ip-admin'),
    path('about/', views.IPabout, name='ip-about'),
    path('home/', views.IPhome, name='ip-home'),
    path('home/simple_function', views.IPsimple_function, name='ip-admin'),
    path('home/simple_function', views.IPsimple_function, name='ip-admin'),
    path('home/simple_function/external', views.IPexternal),
    path('external/', views.IPexternal, name='ip external'),
    path('/external/', views.IPexternal, name='ip external'),
    path('blog/external/', views.IPexternal, name='ip-external'),
    path('home/external/', views.IPexternal, name='home-external'),
    path('', views.IPhome, name='ip-home'), # redirect back home
   # path('', views.home, name='blog-home+nopath'),
    #path('', views.simple_function(), name='simple_function'),
]
