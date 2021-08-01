from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['user', 'image', 'project_title', 'project_summary']


class ChapterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = ['chapter_number', 'file', 'student', 'supervisor']


class AssessChapterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = ['chapter_number', 'file', 'student', 'supervisor', 'supervisor_remarks', 'status']


class RequestMeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = RequestMeeting
		fields = ['date', 'additional_informaton', 'student']


class ProjectStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectStatus
		fields = ['status', 'complete', 'profile']