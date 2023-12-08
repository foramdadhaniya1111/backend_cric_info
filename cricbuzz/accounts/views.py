from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from .serializer import UserSerialzer,RegisterSerializer,LoginSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status

class RegisteraAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            # "user":UserSerialzer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1],
            'msg':'Registraion Successful',
            'status':status.HTTP_201_CREATED
        })
   
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(LoginAPI,self).post(request,format=None)
        
class userview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def get(self ,request):
        serializer = UserSerialzer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 