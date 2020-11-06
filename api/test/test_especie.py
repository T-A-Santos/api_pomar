from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Especies


class EspeciesTestCase(APITestCase):
    def setUp(self):
        Especies.objects.create(descricao='Eucalyptus')

    
    def test_get_method(self):
        url = '/especies/'
        response=self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs=Especies.objects.filter(descricao='Eucalyptus')
        self.assertEqual(qs.count(),1)

    def test_post_method(self):
        url = '/especies/'
        data = {'descricao': 'Laranjeiras'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_post_method_fail(self):
        url = '/especies/'
        data = {'descricao': ''}
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_method(self):
        url = '/especies/1/'
        response=self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_put_method(self):
        url = '/especies/1/'
        data = {'descricao': 'Laranjeira'}
        response=self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['descricao'], 'Laranjeira')
 
    def test_put_method_fail(self):
        url = '/especies/1/'
        data = {'descricao':''}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    