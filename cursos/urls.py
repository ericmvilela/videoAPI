from django.urls import path
from cursos import views

urlpatterns = [
    path("videos/", views.VideoViewSet.as_view(), name="videos"),
    # path("modulos/", views.ModuloViewSet.as_view(), name="modulos"),
    path("categorias/<int:idCat>", views.CategoriaViewSet.as_view(), name="categorias"),
    path("categorias/<int:idCat>/<int:idMod>", views.ModuloViewSet.as_view(), name="categorias"),
    path("categorias/<int:idCat>/<int:idMod>/addvideo", views.VideoViewSet.as_view(), name="categorias"),
    path("categorias/<int:idCat>/<int:idMod>/<int:idVideo>", views.VideoViewSet.as_view(), name="categorias"),
    path("categorias/", views.CategoriaViewSet.as_view(), name="categorias"),
    path("categorias/<int:idCat>/addmodulo", views.ModuloViewSet.as_view(), name="categorias")
]
