from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('superadmin', views.superadmin, name="superadmin"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('admin', views.admin, name="admin"),
    path('signinA', views.signinA, name="signinA"),
    path('lastpage', views.lastpage, name="lastpage"),
]
urlpatterns += staticfiles_urlpatterns()