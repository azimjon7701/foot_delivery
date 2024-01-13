from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from main import serializers

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Invalid refresh token or token not provided."},
                            status=status.HTTP_400_BAD_REQUEST)
