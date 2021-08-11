from django.conf.urls import url
from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.home, name = "home"),
    # path('register/', views.register_candidate, name = "register"),
    path('register/', views.Create_candidato.as_view(), name = "register"),
    path('ofert/', views.Create_ofert.as_view(), name = "ofert"),
    path('oferts/', views.oferts, name = "oferts"),
    # path('empleability/', views.Empleability.as_view(), name = "empleability"),
    path('empleability/', views.empleability, name = "empleability"),
    url(r'^delete/(?P<id>\d+)/$', views.delete_candidato, name = "delete"),
    url(r'^delete1/(?P<id>\d+)/$', views.delete_oferts, name = "delete1"),
    url(r'^update/(?P<pk>\d+)/$', views.Update_candidate.as_view(), name = "update"),
    url(r'^update1/(?P<pk>\d+)/$', views.Update_ofert.as_view(), name = "update1"),
    path('candidate/', views.candidate, name = "candidate"),
    path('error/', views.error, name = "error"),
    # path('m/', views.m, name = "m"),
]