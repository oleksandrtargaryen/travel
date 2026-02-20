# Create your views here.
import asyncio
from drf_yasg.openapi import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.db.models import Q

from .models import Project, Place
from .serializers import ProjectSerializer, PlaceSerializer
from .services.api_services import GooglePlacesOpenWeatherService

class ProjectViewSet(viewsets.ModelViewSet):
    """
    GET /api/projects/ - список
    POST /api/projects/ - створити
    GET /api/projects/1/ - деталі
    PUT /api/projects/1/ - оновити повністю
    PATCH /api/projects/1/ - оновити частково
    DELETE /api/projects/1/ - видалити
    GET /api/projects/search/?q=<text> - пошук по name та description
    """
    queryset = Project.objects.prefetch_related('places')
    serializer_class = ProjectSerializer
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)

        projects = Project.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query))

        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)



class PlaceViewSet(viewsets.ModelViewSet):
    """
    GET /api/places/ - список
    GET /api/places/?project=1 - фільтрація
    POST /api/places/ - створити
    GET /api/places/1/ - деталі
    PUT /api/places/1/ - оновити повністю
    PATCH /api/places/1/ - оновити частково (mark visited)
    DELETE /api/places/1/ - видалити
    """
    queryset = Place.objects.prefetch_related('project')
    serializer_class = PlaceSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

    @action(detail=True, methods=['get'])
    def get_weather(self, place_id, pk = None):
        google_place = self.get_object()
        result = asyncio.run(GooglePlacesOpenWeatherService.async_get_google_place(google_place.google_place_id))
        return Response(result, status=status.HTTP_200_OK)