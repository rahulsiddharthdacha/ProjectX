from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import MyForm
# Create your views here.

class Login(LoginView):
    template_name='Users/login.html'
    form_class=MyForm
    def form_valid(self, form):
        username=form.cleaned_data.get('username')
        messages.success(self.request, f"Welcome To Project X mr.{ username }")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
    
    


class Logout(LogoutView):
    template_name='Users/logout.html'

