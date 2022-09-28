from . import views
from django.urls import path




urlpatterns = [

     path('register',views.registration,name='registration'),
 ]