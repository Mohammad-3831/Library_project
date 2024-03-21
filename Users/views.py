from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions

from .forms import *
from .serializers import *
from rest_framework.response import Response


class GetAllUsersView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        data = UserSerializer(users, many=True)
        return Response(data.data, status=status.HTTP_200_OK)


class GetUserView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        data = UserSerializer(user, many=False)
        return Response(data.data, status=status.HTTP_200_OK)


class AddUserView(APIView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['password1'])
            return Response({'message': 'User added successfully!'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserView(APIView):
    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=self.request.user
        user.delete()

        return Response({"result":"user deleted successfully!"},status=status.HTTP_200_OK)