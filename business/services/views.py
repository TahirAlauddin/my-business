from django.shortcuts import render
from .models import ServicesListModel
# from .forms import (Copies, CM, CaseFiling, Adjournment)
from django.views.generic import ListView

# def ServicesListView(request):
#     return render(request, 'home.html')
    
class ServicesListView(ListView):
    model = ServicesListModel
    template_name = 'home.html'
    context_object_name = 'services_object_list'


def HC_Copies_View(request):
    return render(request, 'hc_copies.html')


def SC_Copies_View(request):
    return render(request, 'sc_copies.html')


def LC_Copies_View(request):
    return render(request, 'lc_copies.html')


def Adjournment_View(request):
    return render(request, 'adjournment.html')


def CM_View(request):
    return render(request, 'cm.html')


def Case_Filing_View(request):
    return render(request, 'case_filing.html')


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')


