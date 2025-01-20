from django.urls import path
from django.http import HttpResponse
from .views import IndexView, RegisterView, LoginView, logout_view, PlataformaView, remove_ip

app_name = 'blacklist'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('plataforma/', PlataformaView.as_view(), name='plataforma'),
    path('remove_ip/<int:ip_id>/', remove_ip, name='remove_ip'),
]
