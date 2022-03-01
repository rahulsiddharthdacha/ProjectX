
from unicodedata import name
from django.urls import path
from .views import Login,Logout
urlpatterns = [
    path('Login/',Login.as_view(),name='login'),
    path('Logout/',Logout.as_view(),name='logout')
]
