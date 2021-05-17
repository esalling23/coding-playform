from django.urls import path

from .views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    path('sign-up/', SignUp.as_view()),
    path('sign-in/', SignIn.as_view()),
    path('sign-out/', SignOut.as_view()),
    path('change-pw/', ChangePassword.as_view()),
]
