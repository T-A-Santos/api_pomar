from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'especies', views.EspeciesViewSet)
router.register(r'arvores', views.ArvoresViewSet)
router.register(r'grupoArvores', views.GrupoArvoresViewSet)
router.register(r'colheita', views.ColheitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]