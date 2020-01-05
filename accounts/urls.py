from django.urls import path
from . import views
from .api import views


urlpatterns = [
    # path('register/', views.Register.as_view(), name='register'),
    path('api/v1/users/', views.UserListView.as_view(), name=None),
]
