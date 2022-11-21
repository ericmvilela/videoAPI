from django.urls import path
from cursos import views

urlpatterns = [
    path("videos/", views.VideoViewSet.as_view(), name="videos"),
    # path("modulos/", views.ModuloViewSet.as_view(), name="modulos"),
    path("curso/<int:idCat>", views.CursoViewSet.as_view(), name="categorias"),
    path("curso/<int:idCat>/<int:idMod>", views.ModuloViewSet.as_view(), name="categorias"),
    path("curso/<int:idCat>/<int:idMod>/addvideo", views.VideoViewSet.as_view(), name="categorias"),
    path("curso/<int:idCat>/<int:idMod>/<int:idVideo>", views.VideoViewSet.as_view(), name="categorias"),
    path("curso/", views.CursoViewSet.as_view(), name="categorias"),
    path("curso/<int:idCat>/addmodulo/", views.ModuloViewSet.as_view(), name="categorias")
]
