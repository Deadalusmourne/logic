#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7
# __author__: caoge
"""gabriel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from logic import views

urlpatterns = [
    url(r'^intime_online_person/', views.intime_online_person, name="intime_online_person"),
    url(r'^test/', views.get_chart),
    url(r'^get_league_match/(\d+)', views.get_league_match_by_id, name="get_league_match_by_id"),
    url(r'^go_test', views.go_test),
    url(r'^update_hero', views.update_hero),
]

