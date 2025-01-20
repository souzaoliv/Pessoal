from django.urls import path
from django.http import HttpResponse
from .views import IndexView, RegisterView

app_name = 'blacklist'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),

]
