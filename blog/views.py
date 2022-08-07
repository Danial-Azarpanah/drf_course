from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def hello_world(request):
    """
    Show user's info that is received in url (Get method). Return a static sentence if it's Post.
    """
    name = request.GET.get('name')
    last_name = request.GET.get('lastname')

    if request.method == 'POST':
        data = request.data
        return Response({'message': f'Hello, {data.get("name")} {data.get("lastname")} FBV POST'})

    return Response({'message': f'Hello, {name} {last_name} from FBV GET'})


class HelloWorld(APIView):
    """
    This class has the same function as the view above
    """

    def get(self, request):
        name = request.GET.get('name')
        last_name = request.GET.get('lastname')
        return Response({'message': f'Hello , {name} {last_name} from CBV GET'})

    def post(self, request):
        data = request.data
        return Response({'message': f'Hello, {data.get("name")} {data.get("lastname")} in CBV POST'})
