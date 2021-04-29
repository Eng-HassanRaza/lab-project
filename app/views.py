# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .models import GeneralHealth,LiverHealth,KidneyHealth,insulin_sensitive,\
    Lipids,Iron,HormonalBalance,BoneHealth,Inflammation,Micronutrients

@login_required(login_url="/login/")
def index(request):
    general_health = GeneralHealth.objects.filter(user=request.user)
    liver_health = LiverHealth.objects.filter(user=request.user)
    kidney_health = KidneyHealth.objects.filter(user=request.user)
    insulin_sensitive_obj = insulin_sensitive.objects.filter(user=request.user)
    Lipids_obj = Lipids.objects.filter(user=request.user)
    Iron_obj = Iron.objects.filter(user=request.user)
    HormonalBalance_obj = HormonalBalance.objects.filter(user=request.user)
    BoneHealth_obj = BoneHealth.objects.filter(user=request.user)
    Inflammation_obj = Inflammation.objects.filter(user=request.user)
    Micronutrients_obj = Micronutrients.objects.filter(user=request.user)
    context = {
        'segment' : 'index',
        'general_health':general_health,
        'liver_health':liver_health,
        'kidney_health':kidney_health,
        'insulin_sensitive_obj':insulin_sensitive_obj,
        'Lipids_obj':Lipids_obj,
        'Iron_obj':Iron_obj,
        'HormonalBalance_obj':HormonalBalance_obj,
        'BoneHealth_obj':BoneHealth_obj,
        'Inflammation_obj':Inflammation_obj,
        'Micronutrients_obj':Micronutrients_obj,
    }
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
