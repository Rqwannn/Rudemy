from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from .models import *
from .serializers import *
from .forms import *
from .utils import *

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

# End Auth Logic

# Developer Page Logic


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ProfileView(request):
    queryset, search_query = SearchProfiles(request)

    serializers = ProfileSerializers(queryset, many=True)
    data = {
        'data': serializers.data,
        'search': search_query,
    }
    return Response(data)

# End Developer Page Logic
