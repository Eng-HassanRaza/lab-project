# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import GeneralHealth,LiverHealth,KidneyHealth,insulin_sensitive,\
    Lipids,Iron,HormonalBalance,BoneHealth,Inflammation,Micronutrients

# Register your models here.

admin.site.register(GeneralHealth)
admin.site.register(LiverHealth)
admin.site.register(KidneyHealth)
admin.site.register(insulin_sensitive)
admin.site.register(Lipids)
admin.site.register(Iron)
admin.site.register(HormonalBalance)
admin.site.register(BoneHealth)
admin.site.register(Inflammation)
admin.site.register(Micronutrients)