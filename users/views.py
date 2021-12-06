from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserSerializer


# class UserListView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
