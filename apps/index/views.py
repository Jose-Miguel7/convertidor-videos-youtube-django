from django.shortcuts import render
from django.views.generic import TemplateView, View

import youtube_dl
import re


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

        ydl_opts = {'nocheckcertificate': True}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(video_url, download=False)

        video_audio_streams = []
        for m in meta.get('formats'):
            file_size = m.get('filesize')
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000,2)} mb'

            resolution = 'Audio'
            if m.get('height') is not None:
                resolution = f"{m['width']}x{m['height']}"
            video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'filesize': file_size,
                'video_url': m['url']
            })
        video_audio_streams = video_audio_streams[::-1]
        context = {
            'title': meta['title'],
            'streams': video_audio_streams,
            'description': meta['description'],
            'likes': meta.get('like_count'),
            'thumb': meta['thumbnails'][3]['url'],
            'duration': round(int(meta['duration'])/60, 2),
            'views': f'{int(meta["view_count"]):,}'
        }
        return render(request, 'index/home.html', context=context)
