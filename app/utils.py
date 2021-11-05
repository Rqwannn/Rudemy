from django.db.models import Q
from .models import *
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def SearchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skill = Tag.objects.filter(name__iexact=search_query)
    dataDev = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skill))

    return dataDev, search_query


def SearchCourse(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    data = Course.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query))

    return data, search_query


class NumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'records'
    max_page_size = 7
    # last_page_strings = 'end'
