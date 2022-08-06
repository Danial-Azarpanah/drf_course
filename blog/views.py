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
        return Response('Hello, I\'m from Post in FBV')

    return Response(f'Hello, {name} {last_name} from FBV')


class HelloWorld(APIView):
    """
    This class has the same function as the view above
    """

    def get(self, request):
        name = request.GET.get('name')
        last_name = request.GET.get('lastname')
        return Response(f'Hello , {name} {last_name} from CBV')

    def post(self, request):
        return Response(f'Hello, I\'m from Post in CBV')
