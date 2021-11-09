from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = '__all__'


class ReviewCourseSerializers(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    course = ReviewCourseSerializers(many=False)

    class Meta:
        model = Review
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer(many=False)
    recipient = ProfileSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'


class APICourseSerializers(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class APIProfileSerializers(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    skill = TagSerializer(many=True)
    course_set = CourseSerializer(many=True)

    class Meta:
        model = Profile
        fields = "__all__"
