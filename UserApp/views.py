from rest_framework import permissions, generics
from rest_framework.viewsets import ModelViewSet

from .models import UserApp
from .serializers import GetUserAppSerializer, GetUserListSerializer


class UserAppListView(generics.ListAPIView):
    """список пользователей"""
    queryset = UserApp.objects.all()
    serializer_class = GetUserListSerializer


class UserAppView(ModelViewSet):
    """вывод пользователя"""
    serializer_class = GetUserAppSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):  # редактирование только своего профиля
        return UserApp.objects.filter(id=self.request.user.id)


