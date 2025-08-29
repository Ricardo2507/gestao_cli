from django.urls import path
from .views import home
from django.contrib.auth import views as   auth_views

app_name='home'

urlpatterns = [
    path('',home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
 
   
]