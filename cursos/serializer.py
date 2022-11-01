from rest_framework import serializers
from cursos.models import Video, Modulo, Categoria


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


class CategoriaSerializer(serializers.ModelSerializer):
    modulos = AllModuloSerializer(many=True)

    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'descricao', 'modulos']


class AllCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'descricao']
