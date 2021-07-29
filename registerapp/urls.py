from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.homePage, name='home'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',views.register, name='register')
]