from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from drf_yasg.utils import swagger_auto_schema


class UserRegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={201: UserRegisterSerializer}
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
