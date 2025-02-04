from django.urls import path
from .views import IndexView, PlataformaView
app_name = 'bruteforce'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('plataforma/', PlataformaView.as_view(), name='plataforma'),
]