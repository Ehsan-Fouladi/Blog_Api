from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegisterUserSerializers, ChangePasswordSerializer, ProfileUserSerializers, ProfileUserUpdateSerializers
from .models import User


class RegisterUserApiView(generics.GenericAPIView):
    """
    Register a new user.
    """
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
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            return Response({'message': 'Password Updated successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUserApiView(generics.RetrieveAPIView):
    """
    Retrieve user profile.
    """
    serializer_class = ProfileUserSerializers

    def get_object(self):
        return self.request.user


class ProfileUserUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    Update User profile.
    """
    serializer_class = ProfileUserUpdateSerializers
    queryset = User.objects.all()
    parser_classes = [MultiPartParser,]
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user
