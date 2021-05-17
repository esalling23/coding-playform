from rest_framework import generics, status
from rest_framework.response import Response

# Model
from ..models.challenge import Challenge

# Serializer
from ..serializers import ChallengeSerializer

class ChallengeList(generics.ListAPIView):
    """
    Displays multiple & creates challenges.
    Includes user ownership.
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ChallengeDetail(generics.RetrieveAPIView):
    """
    Displays one & updates Challenges.
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
