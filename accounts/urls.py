from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .api import views as users_api_views


urlpatterns = [
    # urls are automatically appended with "accounts/URL_PATH_DEFINED_BELOW"
    # path('register/', views.Register.as_view(), name='register'),
    path('api/v1/users/', users_api_views.UserListView.as_view(), name=None),
    path('api/v1/create_user/', users_api_views.UserCreateView.as_view(), name=None),
    path('api/v1/api_token_auth/', obtain_auth_token, name='api_token_auth'),
]
