from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from django.urls import reverse

from api.models import Especies, Arvores
from api.serializers import EspeciesSerializer, ArvoresSerializer


class EspeciesTestCase(APITestCase):
    def setUp(self):
        self.especie = Especies.objects.create(descricao='Eucalyptus')
        Arvores.objects.create(descricao='Eucalyptus Grandis',especies=self.especie, idade=12)

    def test_get_method(self):
        url = '/arvores/'
        response=self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs=Arvores.objects.filter(descricao='Eucalyptus Grandis')
        self.assertEqual(qs.count(),1)
        es=Arvores.objects.filter(especies__descricao='Eucalyptus')
        self.assertEqual(es.count(),1)
    
    def test_delete_method(self):
        url = '/arvores/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
