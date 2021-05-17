from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

# models
from .models.attempt import Attempt
from .models.challenge import Challenge
from .models.test_case import TestCase

from auth.serializers import UserSerializer

class ChallengeSerializer(ModelSerializer):
    """Serializes Challenge model"""
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description')

class AttemptSerializer(ModelSerializer):
    """Serializes Attempt model"""
    owner = PrimaryKeyRelatedField(read_only=True)
    # challenge = ChallengeSerializer()

    class Meta:
        model = Attempt
        fields = ('id', 'owner', 'challenge', 'user_solution', 'passes', 'failures')

class TestCaseSerializer(ModelSerializer):
    """Serializes TestCase model"""
    class Meta:
        model = TestCase
        fields = ('id', 'fn_input', 'fn_output', 'challenge')
        depth = 1
