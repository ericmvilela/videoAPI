from rest_framework import serializers
from cursos.models import Video, Modulo, Curso


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'titulo', 'linkVideo', 'modulo', 'thumbnail']


class ModuloSerializer(serializers.ModelSerializer):
    categoriaNome = serializers.CharField(source='categoria.titulo')
    videos = VideoSerializer(many=True)

    class Meta:
        model = Modulo
        fields = ['id', 'titulo', 'categoria', 'categoriaNome', 'videos']


class AllModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'titulo', 'categoria']


class CursoSerializer(serializers.ModelSerializer):
    modulos = ModuloSerializer(many=True)

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'image', 'descricao', 'modulos']


class AllCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'descricao', 'image']
