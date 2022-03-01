
from os import name
from django.urls import path
from .views import Home,Dashboard,DCmeterAnyalsis
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('WMSAnalysis',Dashboard.as_view(),name='dashbaord'),
    path('DcmeterAnalysis',DCmeterAnyalsis.as_view(),name='dashboard1'),
]
