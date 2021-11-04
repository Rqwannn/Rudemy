from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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


class ProfileAPI(ListAPIView):
    queryset = Profile.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = APIProfileSerializers
    pagination_class = NumberPagination
    api_view = ['GET', 'POST']

    def get_queryset(self):
        if self.request.data.get('search_query'):
            data, search_query = SearchProfiles(self.request)
            self.queryset = data
        elif self.request.GET.get('search_query'):
            data, search_query = SearchProfiles(self.request)
            self.queryset = data
            print(self.queryset)

        return self.queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# End Developer Page Logic
