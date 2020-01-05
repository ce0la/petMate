from django.urls import path
from . import views
from .api import views as api_views


urlpatterns = [
    # main APP paths
    path('', views.index, name='index'),
    path('petdetails/', views.petdetails, name='petdetails'),
    path('petpreview/', views.petpreview, name='petpreview'),
    path('petlisting/', views.petlisting, name='petlisting'),

    # API endpoints paths
    path('api/v1/', api_views.PetListView.as_view(), name=None),
    path('api/v1/create_pet/', api_views.PetCreateView.as_view(), name=None),
    path('api/v1/edit_pet/<int:pk>/', api_views.PetDetailView.as_view(), name=None),
    path('api/v1/upload-image', api_views.UploadView.as_view()),
]