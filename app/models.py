# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GeneralHealth(models.Model):
    full_blood_count = models.IntegerField(max_length=255,null=True,blank=True)
    total_protein = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

class LiverHealth(models.Model):
    liver_function_test = models.IntegerField(max_length=255,null=True,blank=True)
    alkaline_phosphatase = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class KidneyHealth (models.Model):
    creatinine = models.IntegerField(max_length=255,null=True,blank=True)
    urea = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class insulin_sensitive  (models.Model):
    fasting_glucose  = models.IntegerField(max_length=255,null=True,blank=True)
    hba1c = models.IntegerField(max_length=255,null=True,blank=True)
    homa_ir = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Lipids  (models.Model):
    total_cholersterol   = models.IntegerField(max_length=255,null=True,blank=True)
    hdl = models.IntegerField(max_length=255,null=True,blank=True)
    ldl = models.IntegerField(max_length=255,null=True,blank=True)
    triglycerides = models.IntegerField(max_length=255,null=True,blank=True)
    nmr_lipids  = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Iron(models.Model):
    ferritin = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
class HormonalBalance(models.Model):
    tsh = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
class BoneHealth(models.Model):
    calcium = models.IntegerField(max_length=255,null=True,blank=True)
    phosphate  = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Inflammation(models.Model):
    hscrp = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
class Micronutrients(models.Model):
    magnesium = models.IntegerField(max_length=255,null=True,blank=True)
    sodium = models.IntegerField(max_length=255,null=True,blank=True)
    potassium = models.IntegerField(max_length=255,null=True,blank=True)
    vitamin_d3 = models.IntegerField(max_length=255,null=True,blank=True)
    vitamin_b12 = models.IntegerField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
