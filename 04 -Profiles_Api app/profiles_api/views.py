from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ Return a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
