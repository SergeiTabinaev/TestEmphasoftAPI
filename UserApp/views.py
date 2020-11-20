from rest_framework.generics import CreateAPIView
from .models import UserApp
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import CreateUserSerializer, GetUserAppSerializer
from rest_framework.authtoken.models import Token


class RegistrUserView(CreateAPIView):
    queryset = UserApp.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = True
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)



@api_view(['GET'])
@permission_classes(IsAuthenticated,)
def user_list_view(request):
    if request.method == "GET":
        users = UserApp.objects.all()
        serializer = GetUserAppSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes(IsAuthenticated,)
def user_detail_view(request, pk):
    try:
        user_detail = UserApp.objects.get(id=pk)
    except UserApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GetUserAppSerializer(user_detail)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes(IsAuthenticated,)
def user_update_view(request, pk):
    try:
        user_detail = UserApp.objects.get(id=pk)
    except UserApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if UserApp.username != user:
        return Response({'response': "Вы не имеете permissions, для этого"})

    if request.method == "PUT":
        serializer = GetUserAppSerializer(user_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['succes'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes(IsAuthenticated,)
def user_delete_view(request, pk):
    try:
        user_detail = UserApp.objects.get(id=pk)
    except UserApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if UserApp.username != user:
        return Response({'response': "Вы не имеете permissions, для удаления"})

    if request.method == "DELETE":
        operation = user_detail.delete()
        data = {}
        if operation:
            data['succes'] = 'delete successful'
        else:
            data['failture'] = 'delete failed'
        return Response(data=data)




