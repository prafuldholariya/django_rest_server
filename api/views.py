from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # This calls the create method in UserSerializer
        
        return Response({"message": "User created successfully", "user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response(
                {"message": "Login successful"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserDataView(generics.ListAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]  # Optional: restrict access to admin users only

    def get_queryset(self):
        return (
            CustomUser.objects.all()
        ) 