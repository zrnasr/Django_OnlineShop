from rest_framework.views import APIView
from user.models import Profile, User
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from user.api.v1.serializers import ProfileSerializer, LoginSerializer, RegisterSerializer



class ProfilePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'
    def get(self, request):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegisterPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self, request):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


