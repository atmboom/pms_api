from django.shortcuts import render
from rest_framework import serializers
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from .models import *

# Create your views here.
for user in User.objects.all():
	Token.objects.get_or_create(user=user)


class ChapterApiView(APIView):
	def get(self, request, *args, **kwargs):
		chapter_serializer = Chapter.objects.all()
		serializer = ChapterSerializer(chapter_serializer, many=True)
		return Response(serializer.data)


class ChapterCreateApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser]
    serializer_class = ChapterSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChapterUpdateApiView(mixins.UpdateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ChapterSerializer

    def test_func(self):
        chapter = self.get_object()
        if self.request.user == chapter.student:
            return True
        return False


class AssessChapterApiView(mixins.UpdateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AssessChapterSerializer

    # def test_func(self):
    #     chapter = self.get_object()
    #     if self.request.user == chapter.supervisor:
    #         return True
    #     return False


class ProfileApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):        
        profile_serializer = Profile.objects.filter(user=self.request.user)
        serializer = ProfileSerializer(profile_serializer, many=True)
        return Response(serializer.data)    


class ProfileUpdateApiView(mixins.ListModelMixin, generics.UpdateAPIView):    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer    
    queryset = Profile.objects.all()


class MeetingCreateApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser]
    serializer_class = RequestMeetingSerializer

    def perform_create(self, serializer):
        serializer.save(supervisor=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MeetingUpdateApiView(mixins.ListModelMixin, generics.UpdateAPIView):    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RequestMeetingSerializer    
    queryset = RequestMeeting.objects.all()


class StatusApiView(APIView):
	def get(self, request, *args, **kwargs):
		project_serializer = ProjectStatus.objects.all()
		serializer = ProjectStatusSerializer(project_serializer, many=True)
		return Response(serializer.data)


class StatusSerializerApiView(mixins.ListModelMixin, generics.UpdateAPIView):    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectStatusSerializer    
    queryset = ProjectStatus.objects.all()