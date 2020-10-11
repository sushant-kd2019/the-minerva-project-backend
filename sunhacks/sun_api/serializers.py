from rest_framework import serializers
from .models import *

class RoadmapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roadmap
        fields = ('id','creator','r_name','number_of_forks','number_of_courses','details','stars','date')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','roadmap','course_name','course_link','course_description','date')

class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id','user','text','link','date')

class ForkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fork
        fields = ('id','forker','roadmap_id','progress','date')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','nationality','gender','institute','avatar','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','nationality','gender','institute','avatar','email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.nationality = validated_data['nationality']
        user.gender = validated_data['gender']
        user.institute = validated_data['institute']
        user.avatar = validated_data['avatar']
        return user