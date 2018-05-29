from django.urls import path,include
from .views import *
app_name='user'





urlpatterns = [
    # path('frame/',frame),
    path('login/',login),
    path('home1/',home1),
    path('register/',register),
    path('options/',options),
    path('pay/',pay),

]
