from re import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import WMS,DCmeter
# Create your views here.

class Dashboard(LoginRequiredMixin,ListView):
    model=WMS
    template_name='dashboard/index.html'
    context_object_name='home'

class Home(TemplateView):
    template_name='partials/base.html'

class DCmeterAnyalsis(LoginRequiredMixin,ListView):
    model=DCmeter
    template_name=template_name='dashboard/dcmeter.html'
    context_object_name='dcm'

