from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q
from .models import *
from .serializers import *
from .forms import *
from .utils import *
import os

# Create your views here.

# Auth Logic


@api_view(['POST'])
def RegisterUser(request):
    form = RegisterForm(request.data)
    if form.is_valid():
        auth = form.save()
        data = {
            "status": True,
            "message": "User Account Was Created"
        }

        return Response(data)

    else:
        data = {
            "status": False,
            "message": "Something Went Wrong"
        }

        return Response(data)


@api_view(['POST'])
def LoginAuthentication(request):
    CekUsername = True
    usernameField = request.data.get('username')
    passwordField = request.data.get('password')

    try:
        data = User.objects.get(username=usernameField)
    except:
        CekUsername = False

    user = authenticate(request, username=usernameField,
                        password=passwordField)

    serializers = UserSerializer(data, many=False)

    if CekUsername:
        if user is not None:
            login(request, user)
            Data = {
                'UserData': serializers.data,
                'status': True
            }
        else:
            Data = {
                'messages': 'Password Incorrect',
                'status': False
            }
    else:
        Data = {
            'messages': 'Username Not Found',
            'status': False
        }

    return Response(Data)


# End Auth Logic

# Developer Page Logic


class ProfileAPI(ListAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = APIProfileSerializers
    pagination_class = NumberPagination
    api_view = ['GET', 'POST']

    def get_queryset(self):
        if self.request.GET.get('search_query'):
            data, search_query = SearchProfiles(self.request)
            self.queryset = data
            print(self.queryset)

        return self.queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSingleUser(request, user):
    data = Profile.objects.get(user=user)
    serializer = APIProfileSerializers(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserProfile(request, pk):
    try:
        profile = request.user.profile
    except:
        profile = None

    try:
        dataDev = Profile.objects.get(id=pk)
        serializer = APIProfileSerializers(dataDev, many=False)
        profile_serializer = ProfileSerializer(profile, many=False)

        data = {
            'data': serializer.data,
            'profile': profile_serializer.data
        }

        return Response(data)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Not Found')
    except ValidationError:
        return HttpResponseNotFound('Not Found')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUser(request):
    user = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=user)

    ProfileData = {
        'name': request.data.get('name'),
        'location': request.data.get('location'),
        'short_intro': request.data.get('short_intro'),
        'bio': request.data.get('bio'),
    }

    form = ProfileForm(ProfileData, instance=user)

    if form.is_valid():

        change = form.save(commit=False)
        change.user.email = request.data.get('email')
        change.user.username = request.data.get('username')
        form.save()

        context = {
            'status': True,
            'message': 'User Berhasil Di Update'
        }

        return Response(context)

# End Developer Page Logic

# Course Logic


class CourseAPI(ListAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = APICourseSerializers
    pagination_class = NumberPagination
    api_view = ['GET', 'POST']

    def get_queryset(self):
        if self.request.GET.get('search_query'):
            data, search_query = SearchCourse(self.request)
            self.queryset = data

        return self.queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserCourse(request, pk):
    try:
        profile = request.user.profile
    except:
        profile = None

    try:
        dataCourse = Course.objects.get(id=pk)
        serializer = CourseSerializer(dataCourse, many=False)
        profile_serializer = ProfileSerializer(profile, many=False)

        data = {
            'data': serializer.data,
            'profile': profile_serializer.data,
            'authenticated': request.user.is_authenticated
        }

        return Response(data)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Not Found')
    except ValidationError:
        return HttpResponseNotFound('Not Found')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ReviewCourse(request):
    AllData = Course.objects.get(id=request.data.get('id'))

    insertData = {
        'value': request.data.get('value'),
        'body': request.data.get('body'),
    }

    form = ReviewForm(insertData)
    review = form.save(commit=False)
    review.course = AllData
    review.owner = request.user.profile
    review.save()

    AllData.getVoteCount

    return Response('Success')

# End Course Logic

# Inbox Logic


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMessage(request, pk):
    profile = Profile.objects.get(user=pk)
    data = profile.messages.all()
    unread = data.filter(is_read=False).count()

    serializer = MessageSerializer(data, many=True)
    context = {
        'data': serializer.data,
        'unred': unread
    }
    return Response(context)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userMessage(request, pk):
    try:
        profile = request.user.profile
        data = profile.messages.get(id=pk)

        if data.is_read == False:
            data.is_read = True
            data.save()

        serializer = MessageSerializer(data, many=False)

        return Response(serializer.data)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Not Found')
    except ValidationError:
        return HttpResponseNotFound('Not Found')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def InsertMessage(request):
    recipient = Profile.objects.get(id=request.data.get('id'))

    try:
        sender = request.user.profile
    except:
        sender = None

    setRequest = {
        'name': request.data.get('name'),
        'email': request.data.get('email'),
        'subject': request.data.get('subject'),
        'body': request.data.get('body')
    }

    form = MessageForm(setRequest)

    if form.is_valid():
        form = form.save(commit=False)
        form.sender = sender
        form.recipient = recipient

        if sender:
            form.name = sender.name
            form.email = sender.user.email

        form.save()

        result = {
            'Pesan': "Your Message Has Been Send",
            'IdentityUser': recipient.id
        }

        return Response(result)

# End Inbox Logic

# Skill Logic


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def InsertSkill(request):
    account = request.user.profile
    newskills = request.data.get('newskills').replace(',', " ").split()

    for result in newskills:
        tag, created = Tag.objects.get_or_create(name=result)
        account.skill.add(tag)

    context = {
        'status': True,
        'message': 'Skill Has Benn Added'
    }

    return Response(context)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteSkill(request, pk):
    # ~Q => NOT Equal ( != )
    # getSkill = profile.skill.filter(~Q(id=pk))

    profile = request.user.profile
    profile.skill.remove(pk)

    context = {
        'status': True,
        'message': 'Data Has Been Deleted'
    }

    return Response(context)

# End Skill Logic
