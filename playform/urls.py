from django.urls import path

# Routes
from .routes.attempt_routes import AttemptList, AttemptDetail
from .routes.challenge_routes import ChallengeList, ChallengeDetail

urlpatterns = [
    path('attempts/', AttemptList.as_view()),
    path('attempts/<int:pk>/', AttemptDetail.as_view()),
    path('challenges/', ChallengeList.as_view()),
    path('challenges/<int:pk>/', ChallengeDetail.as_view()),
]
