from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .selectors import get_all_users, get_user_by_id
from .services import create_user, update_user, delete_user


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        users = get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = get_user_by_id(pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UserSerializer(user).data)

    def update(self, request, pk=None):
        user = get_user_by_id(pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = update_user(user, serializer.validated_data)
        return Response(UserSerializer(user).data)

    def destroy(self, request, pk=None):
        user = get_user_by_id(pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        delete_user(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
