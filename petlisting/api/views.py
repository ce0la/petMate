from ..models import Petlisting
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Image upload to cloudinary
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader


class UploadView(generics.CreateAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetImageSerializer
    permission_classes = (IsAuthenticated, )

    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        file = request.data.get('pet_image')

        upload_data = cloudinary.uploader.upload(file)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": 'Successfully created',
            "data": upload_data,
        }
        return Response(response)


class PetListView(generics.ListAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = (IsAuthenticated, )


class PetCreateView(generics.CreateAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        super(PetCreateView, self).create(request, *args, **kwargs)
        # create should not have the arguments below
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data
        }
        return Response(response)


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Petlisting.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = (IsAuthenticated, )

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

    def destroy(self, request, *args, **kwargs):
        super(PetDetailView, self).destroy(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully deleted",
            "result": data
        }
        return Response(response)