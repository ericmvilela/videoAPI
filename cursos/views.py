from cursos.serializer import VideoSerializer, ModuloSerializer, CursoSerializer, AllCursoSerializer, \
    AllModuloSerializer
from rest_framework import views, permissions, response
from cursos.models import Video, Modulo, Curso
from accounts.authentication import CustomUserAuthentication
from urllib.parse import urlparse, parse_qs


class VideoViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (CustomUserAuthentication,)

    def get(self, request, idCat=None, idMod=None, idVideo=None):
        video = Video.objects.filter(id=idVideo, modulo=idMod).first()

        if not video:
            return response.Response({'message': 'Id inválido'}, status=400)

        serializer = VideoSerializer(video)

        return response.Response(serializer.data)

    def post(self, request, idCat=None, idMod=None):
        modulo = Modulo.objects.filter(id=idMod, categoria=idCat).first()
        if not modulo:
            return response.Response({'message': 'Id inválido'}, status=400)

        if not 'titulo' in request.data:
            return response.Response({'titulo': 'Esse campo é obrigatório'}, status=400)
        if not 'linkVideo' in request.data:
            return response.Response({'linkVideo': 'Esse campo é obrigatório'}, status=400)

        idVideo = self.videoId(request.data['linkVideo'])
        link = 'https://www.youtube.com/watch?v=' + idVideo

        moduloData = {'modulo': idMod,
                      'titulo': request.data['titulo'],
                      'linkVideo': link,
                      'thumbnail': 'https://i3.ytimg.com/vi/' + idVideo + '/maxresdefault.jpg'}

        serializer = VideoSerializer(data=moduloData)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        newVideo = Video(**data)
        newVideo.save()
        serializer = VideoSerializer(newVideo)

        return response.Response(serializer.data, 201)

    def videoId(self, value):
        query = urlparse(value)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        return None


class ModuloViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (CustomUserAuthentication,)

    def get(self, request, idCat=None, idMod=None):
        modulo = Modulo.objects.filter(id=idMod, categoria=idCat).first()

        if not modulo:
            return response.Response({'message': 'Id inválido'}, status=400)

        serializer = ModuloSerializer(modulo)
        return response.Response(serializer.data)

    def post(self, request, idCat):
        categoria = Curso.objects.filter(id=idCat)
        if not categoria:
            return response.Response({'message': 'Id inválido'}, status=400)

        if not 'titulo' in request.data:
            return response.Response({'titulo': 'Esse campo é obrigatório'}, status=400)

        moduloData = {'categoria': idCat,
                      'titulo': request.data['titulo']}

        serializer = AllModuloSerializer(data=moduloData)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        newModulo = Modulo(**data)
        newModulo.save()
        serializer = AllModuloSerializer(newModulo)

        return response.Response(serializer.data, 201)


class CursoViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (CustomUserAuthentication,)

    def get(self, request, idCat=0):
        if idCat == 0:
            serializer = AllCursoSerializer(Curso.objects.all(), many=True)
            return response.Response(serializer.data)

        else:
            serializer = CursoSerializer(Curso.objects.filter(id=idCat).first())
            return response.Response(serializer.data)

    def post(self, request):
        serializer = AllCursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        newCurso = Curso(**data)
        newCurso.save()
        serializer = AllCursoSerializer(newCurso)

        return response.Response(serializer.data, 201)
