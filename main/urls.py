"""mysite URL Configuration

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
from django.urls import path
from main import views

urlpatterns = [
    # path('', views.fetch_page,name='home page'),
    path('', views.rock_paper_scissor,name='home page'),
    path('guess_number/', views.guess_number,name='guess number'),
    path('test/',views.test_API,name='test'),
    path('time/',views.time,name='clock'),
    path('created/',views.time_since_created,name='created')
]
