from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from pytube import YouTube
import re

class GetVideoInfoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        video_url = request.query_params.get('url', '')
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'

        if not re.match(regex, video_url):
            return Response({'error': 'La solicitud es incorrecta.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            yt = YouTube(video_url)
        except Exception as e:
            return Response({'error': 'El video no se pudo encontrar.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            formats = []
            streams = yt.streams.filter(progressive=True).all() + yt.streams.filter(adaptive=True).all()
            for stream in streams:
                resolution = 'Audio' if not stream.resolution else stream.resolution
                formats.append({
                    'resolution': resolution,
                    'extension': stream.subtype,
                    'filesize': f'{round(stream.filesize / 1000000, 2)} mb' if stream.filesize else 'Unknown',
                    'video_url': stream.url
                })

            data = {
                'title': yt.title,
                'description': yt.description,
                'thumbnail': yt.thumbnail_url,
                'channel_id': yt.channel_id,
                'channel_url': yt.channel_url,
                'publish_date': yt.publish_date.isoformat(),
                'views': yt.views,
                'duration': round(yt.length / 60, 2),
                'keywords': yt.keywords,
                'author': yt.author,
                'formats': formats,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Hubo un error en el servidor.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
