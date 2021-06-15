from django.db import models
# from .forms import *
    
class ServicesListModel(models.Model):
    hc_copies = models.CharField(max_length=255)
    sc_copies = models.CharField(max_length=255)
    lc_copies = models.CharField(max_length=255)
    adjournment = models.CharField(max_length=255)
    case_filing = models.CharField(max_length=255)
    cm = models.CharField(max_length=255)
    hc_copies = models.CharField(max_length=255)
    


class HCCopy(models.Model):
    case_no = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pucca = models.DateField()
    kuccha = models.DateField()
    judges = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=20)

class SCCopy(models.Model):
    case_no = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pucca = models.DateField()
    kuccha = models.DateField()
    judges = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=20)

class LCCopy(models.Model):
    case_no = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pucca = models.DateField()
    kuccha = models.DateField()
    judges = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=20)

class Adjournment(models.Model):
    pass

class CM(models.Model):
    pass

class CaseFiling(models.Model):
    pass

