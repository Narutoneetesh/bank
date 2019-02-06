from django.urls import path
from . import views
urlpatterns= [
    path('credit/',views.credit) ,
    path('debit/',views.debit) ,
    path('logout/',views.logout) ,
    path('edit_profile/',views.profile) ,
    path('check_bal/',views.bal) ,
    ]