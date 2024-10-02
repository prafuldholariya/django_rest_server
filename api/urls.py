from django.urls import path
from .views import RegisterView, LoginView, UserDataView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserDataView.as_view(), name='user-data'),
]