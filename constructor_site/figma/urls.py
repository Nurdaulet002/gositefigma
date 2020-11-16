from django.urls import path
from . import views

app_name = 'figma'
urlpatterns = [
    path('',views.ClientIndexView.as_view(), name ='index'),

    
] 
