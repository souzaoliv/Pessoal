from django.urls import path
from django.http import HttpResponse
from .views import IndexView, RegisterView, LoginView

app_name = 'blacklist'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
   
]
