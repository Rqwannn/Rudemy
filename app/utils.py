from django.db.models import Q
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def SearchProfiles(request):
    search_query = ''

    if request.data.get('search_query'):
        search_query = request.data.get('search_query')

    skill = Tag.objects.filter(name__iexact=search_query)
    dataDev = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skill))

    return dataDev, search_query
