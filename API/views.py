from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doctor,Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer, DoctorSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import get_object_or_404      
from rest_framework import status
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def apiOverview(request):
    api_urls = [
        {'desc':'returns the list of all the user',
         'url':'/user-list/'},
        {'desc':'create a new user',
         'url':'/user-create/'},
        {'desc':'login a user',
         'url':'/user-login/'},
        {'desc':'test token authentication',
         'url':'/test-token/'},
        {'desc':'update an existing user',
         'url':'/user-update/<str:pk>/'},
        {'desc':'delete an existing user',
         'url':'/user-delete/<str:pk>/'},
        {'desc':'get the list of all doctors',
         'url':'/doctors/'},
        
    ]
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all() 
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def userLogin(request):
    user = get_object_or_404(User, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def testToken(request):
    return Response("passed for {}".format(request.user.email))


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def userUpdate(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        if 'password' in request.data:
            user.set_password(request.data['password'])
            user.save()
        return Response({"user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def userDelete(request, pk):
    user = get_object_or_404(User, id=pk )
    user.delete()
    return Response({"details":"deleted successfully :"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getDoctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many = True)
    return Response(serializer.data)