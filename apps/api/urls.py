from django.urls import path

from .views import GetVideoInfoView

urlpatterns = [
    path('convertir/', GetVideoInfoView.as_view(), name='get_video_info'),
]
