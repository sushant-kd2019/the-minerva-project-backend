from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from knox.models import AuthToken
from rest_framework import generics
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from .serializers import *
from .models import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class RoadmapViewSet(viewsets.ModelViewSet):
    queryset = Roadmap.objects.all().order_by('date')
    serializer_class = RoadmapSerializer

    @api_view(['GET',])
    def search_roadmap_public(self,argument):
        queryset = Roadmap.objects.all().filter(roadmap__icontains=argument)
        serializer = RoadmapSerializer(queryset)
        json = JSONRenderer().render(serializers.serializer.data)
        return Response(data=json)
    
    @api_view(['GET'],)
    def search_roadmap_user(self, user, argument):
        queryset = Roadmap.objects.all().filter(creator=user.name).filter(r_name__icontains=argument)
        serializer = RoadmapSerializer(queryset)
        json = JSONRenderer().render(serializers.serializer.data)
        return Response(data=json)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all().order_by('date')
    serializer_class = AchievementSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('date')
    serializer_class = CourseSerializer

class ForkViewSet(viewsets.ModelViewSet):
    queryset = Fork.objects.all().order_by('date')
    serializer_class = ForkSerializer
'''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        fork = serializer.save()
        f = fork.forker()
'''


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

