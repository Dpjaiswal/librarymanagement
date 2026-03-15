"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('/accounts/login/', include('django.contrib.auth.urls')),

    path('adminclick_view', views.adminclick_view, name='adminclick_view'),
    path('studentclick_view', views.studentclick_view, name='studentclick_view'),


    path('adminsignup_view', views.adminsignup_view,name='adminsignup_view'),
    path('studentsignup_view', views.studentsignup_view, name='studentsignup_view'),
    path('adminlogin', LoginView.as_view(
        template_name='library/adminlogin.html'), name='adminlogin'),

    path('studentlogin', LoginView.as_view(
        template_name='library/studentlogin.html'), name='studentlogin'),


    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin_student', views.afterlogin_student,name='afterlogin_student'),
    path('afterlogin',views.afterlogin, name='afterlogin'),

    path('addbook_view', views.addbook_view, name='addbook_view'),
    path('viewbook_view', views.viewbook_view, name='viewbook_view'),
    path('issuebook_view', views.issuebook_view, name='issuebook_view'),
    path('viewissuedbook_view', views.viewissuedbook_view, name='viewissuedbook_view'),
    path('viewstudent_view', views.viewstudent_view, name='viewstudent_view'),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent, name='viewissuedbookbystudent'),

    path('aboutus/', views.aboutus_view),
    path('contactus/', views.contactus_view),
]
