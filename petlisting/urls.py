from django.urls import path
from . import views
from .api import views as pet_api_views


urlpatterns = [
    # main APP paths
    path('', views.index, name='index'),
    path('petdetails/', views.petdetails, name='petdetails'),
    path('petpreview/', views.petpreview, name='petpreview'),
    path('petlisting/', views.petlisting, name='petlisting'),

    # API endpoints paths
    path('api/v1/pets/', pet_api_views.PetListView.as_view(), name=None),
    path('api/v1/create_pet/', pet_api_views.PetCreateView.as_view(), name=None),
    path('api/v1/edit_pet/<int:pk>/', pet_api_views.PetDetailView.as_view(), name=None),
    path('api/v1/upload_pet_image/', pet_api_views.UploadView.as_view()),
]