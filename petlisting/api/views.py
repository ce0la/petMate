from ..models import Petlisting
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


# Image upload to cloudinary
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader


class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        file = request.data.get('pet_image')

        upload_data = cloudinary.uploader.upload(file)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)


class PetListView(generics.ListAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer


class PetCreateView(generics.CreateAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer

    def create(self, request, *args, **kwargs):
        super(PetCreateView, self).create(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data
        }
        return Response(response)


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PetDetailView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "result": data
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PetDetailView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully updated",
            "result": data
        }
        return Response(response)