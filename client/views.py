from django.contrib.auth import logout
from .serializers import UserSerializer, SignInOutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

@api_view(["POST"])
# @permission_classes([~IsAuthenticated])
def signup(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        # serializer.validated_data['is_active'] = False
        user = serializer.save()
        # send_confirmation_email.delay(UserSerializer(user, many=False).data)
        return Response({"data":serializer.data, "message":'None'}, status=status.HTTP_200_OK)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class SignInOutView(APIView):

    def get_permissions(self):
        method = self.request.method
        if method == 'DELETE':
            return  [IsAuthenticated()]
        return []

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is None:
            return Response({'error':"Parol yoki login noto'g'ri!"}, status=status.HTTP_400_BAD_REQUEST)
        token, create = Token.objects.get_or_create(user=user)
        return Response({"token":token.key, "user":{'username':user.username,'id':user.id}}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        if request.user.is_authenticated:
            if request.auth != None:
                request.auth.delete()
            else:
                logout(request)
            return Response({"data":"Come back soon!"}, status=status.HTTP_200_OK)
        return Response({"data":"Something wrong!"}, status=status.HTTP_401_UNAUTHORIZED)
