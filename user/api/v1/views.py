from rest_framework.views import APIView
from user.models import Profile, User
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from user.api.v1.serializers import LoginSerializer, RegisterSerializer, ProfileSerializer

class ProfilePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'
    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many = True)
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DoLogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():

            phone = request.POST['phone']
            password = request.POST['password']
            print(phone)
            print(password)
            user = authenticate(phone = phone, password = password)
            if user is None:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            
            if user.is_staff == True:
                login(request, user)
            else:
                token = Token.objects.get(user=user)
                response = {
                "status": status.HTTP_200_OK,
                "data": {"token" : token.key}
                }
                return Response(response, status = status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class LoginPage(APIView):
    template_name = 'login.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response({'serializer': serializer})

       
    
class RegisterPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self, request):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


