from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('convert', views.GetVideoView.as_view(), name='convert'),
    path('terminos', views.TerminosView.as_view(), name='terminos'),
    path('api', views.HomeAPIView.as_view(), name='api'),
    path('acceso', views.LoginView.as_view(), name='login'),
    path('registro', views.RegisterView.as_view(), name='register'),
]
