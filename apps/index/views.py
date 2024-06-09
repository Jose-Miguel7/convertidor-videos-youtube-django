from django.shortcuts import render
from django.views.generic import TemplateView, View
from pytube import YouTube
import re
import ssl
from urllib.request import urlopen

# Create an unverified context for SSL
ssl._create_default_https_context = ssl._create_unverified_context


class HomeView(TemplateView):
    template_name = 'index/home.html'


class TerminosView(TemplateView):
    template_name = 'index/terminos.html'


class HomeAPIView(TemplateView):
    template_name = 'index/api.html'


class LoginView(TemplateView):
    template_name = 'login.html'
    extra_context = {'login': True}


class RegisterView(TemplateView):
    template_name = 'login.html'
    extra_context = {'login': False}


class GetVideoView(View):
    def post(self, request):
        video_url = request.POST.get('url', '')
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'

        if not re.match(regex, video_url):
            return render(request, 'index/home.html', context={})

        try:
            yt = YouTube(video_url)
        except Exception as e:
            return render(request, 'index/home.html', context={'error': str(e)})
    
        try:
            video_audio_streams = []
            # Filter streams by both progressive and adaptive to get more formats
            streams = yt.streams.filter(progressive=True).all() + yt.streams.filter(adaptive=True).all()
            for stream in streams:
                file_size = stream.filesize
                if file_size:
                    file_size = f'{round(file_size / 1000000, 2)} mb'
                else:
                    file_size = 'Unknown size'

                resolution = 'Audio'
                if stream.resolution:
                    resolution = f"{stream.resolution}"

                video_audio_streams.append({
                    'resolution': resolution,
                    'extension': stream.subtype,
                    'filesize': file_size,
                    'video_url': stream.url
                })

            context = {
                'title': yt.title,
                'streams': video_audio_streams,
                'description': yt.description,
                'thumb': yt.thumbnail_url,
                'duration': round(yt.length / 60, 2),
                'views': f'{yt.views:,}'
            }
            return render(request, 'index/home.html', context=context)
        except Exception as e:
            print(e)
            return render(request, 'index/home.html', context={'error': str(e)})
