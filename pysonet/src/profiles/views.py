from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer

from django.http import HttpResponse


def index(request):
    return HttpResponse("Это страница заглушка.")

class UserNetPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetPrivateView(ModelViewSet):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)

