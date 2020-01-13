from ..models import CustomUser
from ..forms import CustomUserCreationForm, CustomUserChangeForm
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


# Image upload to cloudinary
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, JSONParser

# import cloudinary.uploader


# class UploadView(APIView):
#     parser_classes = (
#         MultiPartParser,
#         JSONParser,
#     )

#     @staticmethod
#     def post(request):
#         file = request.data.get('picture')

#         upload_data = cloudinary.uploader.upload(file)
#         return Response({
#             'status': 'success',
#             'data': upload_data,
#         }, status=201)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        super(UserCreateView, self).create(request, *args, **kwargs)
        # create should not have the arguments below
        # instance = self.get_object()
        # serializer = self.get_serializer()
        # data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data}
        return Response(response)


    # def retrieve(self, request, *args, **kwargs):
    #     super(UserRetrieveView, self).retrieve(request, *args, **kwargs)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     data = serializer.data
    #     response = {
    #         "status_code": status.HTTP_200_OK,
    #         "message": "Successfully retrieved",
    #         "result": data
    #     }
    #     return Response(response)
