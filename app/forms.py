from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place Your Vote',
            'body': 'Add A Comment With Your Vote'
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'short_intro', 'bio']


class EditUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
