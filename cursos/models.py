from django.db import models


def filePath(instance, filename):
    return f'{instance.modulo.categoria.id}/{instance.modulo.id}/{filename}'


class Categoria(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    descricao = models.CharField(max_length=255, null=True, blank=True, verbose_name='Descrição')

    criadoEm = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Modulo(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    categoria = models.ForeignKey(Categoria, related_name='modulos', on_delete=models.CASCADE, verbose_name='Categoria')

    criadoEm = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    linkVideo = models.URLField(null=False, blank=False, verbose_name='Link do Vídeo')
    modulo = models.ForeignKey(Modulo, related_name='videos', on_delete=models.CASCADE, verbose_name='Módulo')
    thumbnail = models.URLField(verbose_name='Link Thumb')

    criadoEm = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
