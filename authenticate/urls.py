from django.urls import path
from .views import IndexView, RegisterView, LoginView, logout_view, PlataformaView

app_name = 'authenticate'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('plataforma/', PlataformaView.as_view(), name='plataforma'),
]