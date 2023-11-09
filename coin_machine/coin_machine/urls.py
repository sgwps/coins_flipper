"""
URL configuration for coin_machine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import main.views



urlpatterns = [
    path('', main.views.index),
    path('machine/', main.views.machine_view),
    path('flip_a_coin/', main.views.flip_a_coin),
    path('get_probability_by_counts/', main.views.get_probability)
]

handler400 = 'main.views.handler400'