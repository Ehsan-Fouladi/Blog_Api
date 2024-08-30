from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegisterUserSerializers, ChangePasswordSerializer, ProfileUserSerializers, ProfileUserUpdateSerializers
from .models import User


class RegisterUserApiView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializers
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = self.get_serializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordApiView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileUserApiView(generics.RetrieveAPIView):
    serializer_class = ProfileUserSerializers

    def get_object(self):
        return self.request.user


class ProfileUserUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProfileUserUpdateSerializers
    parser_classes = (MultiPartParser,)

    def get_object(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except User.DoesNotExist:
            raise NotFound("User Does Not Found Please Try")
        return user
