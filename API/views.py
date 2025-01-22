from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'users': '/user-list/',
        'user-create': '/user-create/',
        
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serailizer = UserSerializer(data = request.data)
    if serailizer.is_valid():
        serailizer.save()
        return Response(serailizer.data)
    return Response(serailizer.error_messages)