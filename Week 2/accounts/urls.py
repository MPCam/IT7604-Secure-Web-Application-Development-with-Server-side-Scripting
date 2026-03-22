from django.urls import path
from .views import SignUpView, SignInView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='sign_in')
]