"""Gym_progression URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include,path
from tasks import views

urlpatterns = [
    
    #path("polls/",include('polls.urls')),
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('tasks/',views.tasks, name='tasks'),
    path('tasks/create/',views.create_record, name='create_record'),
    path('tasks/<int:record_id>/',views.record_detail, name='record_detail'),
    path('tasks/<int:record_id>/delete',views.delete_record, name='delete_record'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    
]
