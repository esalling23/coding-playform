from rest_framework import generics, status
from rest_framework.response import Response

# Model
from ..models.attempt import Attempt

# Serializer
from ..serializers import AttemptSerializer

# Permissions
from ..permissions import UserOwnershipPermission

class AttemptList(generics.ListCreateAPIView):
    """
    Displays multiple & creates attempts.
    Includes user ownership.
    """
    serializer_class = AttemptSerializer

    def get_queryset(self):
        user = self.request.user
        return user.challenge_attempts.all()

    def perform_create(self, serializer):
        # Set user ownership
        serializer.save(owner=self.request.user)

class AttemptDetail(generics.RetrieveUpdateAPIView):
    """
    Displays one & updates attempts.
    """
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = (UserOwnershipPermission,)
