from django.urls import path
from .views import SigninView, RegisterView, MeView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('me/', MeView.as_view(), name='me'),
]
