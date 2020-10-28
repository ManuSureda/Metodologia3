"""init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from .views import index, filter, detail, reserve, login, logout, register, my_reserved_properties

urlpatterns = [
    path('', index, name='index'),
    path('filter/', filter, name='filter'),
    path('detail/<int:id>/', detail, name='detail'),
    path('reserve/<int:id>/', reserve, name='thanks'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('my_reserved_properties', my_reserved_properties, name='my_reserved_properties'),
]
