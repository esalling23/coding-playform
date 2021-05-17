from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout

from .serializers import UserSerializer, UserRegisterSerializer,  ChangePasswordSerializer
from .models import User

class SignUp(generics.CreateAPIView):
    """
    View for user sign up
    Requires password confirmation
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        # Validate password and password confirmation
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid():
            # Validate user data & perform create
            created_user = UserSerializer(data=user.data)
            if created_user.is_valid():
                # Save and send response
                created_user.save()
                return Response(created_user.data, status=status.HTTP_201_CREATED)
            else:
                return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    """
    View for user sign in
    Generates and assigns user authentication token
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request):
        creds = request.data
        user = authenticate(request, email=creds['email'], password=creds['password'])
        # Is our user is successfully authenticated
        if user is not None:
            # And they're active
            if user.is_active:
                # Log them in
                login(request, user)
                # Finally, return a response with the user's token
                return Response({
                    'id': user.id,
                    'email': user.email,
                    'token': user.get_auth_token()
                })
            else:
                return Response({ 'msg': 'The account is inactive.' }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SignOut(generics.DestroyAPIView):
    """
    View for user sign out
    Removes authentication token
    """
    def delete(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied('Please sign in')
        # Remove this token from the user
        request.user.delete_token()
        # Logout will remove all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePassword(generics.UpdateAPIView):
    """
    Endpoint for changing the user's password
    """
    def patch(self, request):
        user = request.user
        # Pass data through serializer
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data['old']):
                raise PermissionDenied('Incorrect password')

            user.set_password(serializer.data['new'])
            user.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)