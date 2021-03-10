from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Account
from users.serializers import RegistrationSerializer


class AccountView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, version):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def post(self, request, version):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request, version):
    try:
        user = Account.objects.get(username=request.data['username'])
    except:
        return Response(
            {"success": False, "errors": ["Invalid username or password"], "status_code": 1,
             "status_message": "fail",
             "message": "Invalid username or password",
             "data": None}, status=status.HTTP_200_OK)
    if not check_password(request.data['password'], user.password):
        return Response(
            {"success": False, "errors": ["Invalid username or password"], "status_code": 1,
             "status_message": "fail",
             "message": "Invalid username or password",
             "data": None}, status=status.HTTP_200_OK)
    else:
        user = Account.objects.get(email=request.data['email'])
        refresh = RefreshToken.for_user(user)
        auth_details = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),

        }
        return Response(
            {"success": True, "errors": None, "status_code": 0,
             "status_message": "success",
             "message": "successfully authenticated user",
             "data": auth_details}, status=status.HTTP_200_OK)
