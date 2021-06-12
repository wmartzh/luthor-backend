from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializer import UserSerializer


@api_view(['POST'])
def register(request):
    try:

        newUser = UserSerializer(data=request.data)
        if not 'password_confirm' in request.data:
            return Response(data={'password_confirm': 'this field is required'}, status=400)

        if not newUser.is_valid():
            return Response(data=newUser.errors, status=400)

        if request.data['password'] != request.data['password_confirm']:
            return Response(data={'password': 'password does not match'}, status=400)

        newUser.save()

        return Response(data={'success': 'user was created successfully'}, status=200)
    except Exception as exception:
        return Response(data="Error: {}".format(exception), status=500)
