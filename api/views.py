from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import (
    EspeciesSerializer,
    ArvoresSerializer,
    GrupoArvoresSerializer,
    ColheitaSerializer,
)
from .models import ( 
    Especies,
    Arvores,
    GrupoArvores,
    Colheita,
)


class EspeciesViewSet(viewsets.ModelViewSet):

    queryset = Especies.objects.all()
    serializer_class = EspeciesSerializer


class ArvoresViewSet(viewsets.ModelViewSet):

    queryset = Arvores.objects.all()
    serializer_class = ArvoresSerializer

class ArvoresDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Arvores.objects.all()
    serializer_class = ArvoresSerializer


class GrupoArvoresViewSet(viewsets.ModelViewSet):

    queryset = GrupoArvores.objects.all()
    serializer_class = GrupoArvoresSerializer


class ColheitaViewSet(viewsets.ModelViewSet):

    queryset = Colheita.objects.all()
    serializer_class = ColheitaSerializer

