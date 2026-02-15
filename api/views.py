# Create your views here.
from rest_framework import viewsets
from .models import Project, Place
from .serializers import ProjectSerializer, PlaceSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    GET /api/projects/ - список
    POST /api/projects/ - створити
    GET /api/projects/1/ - деталі
    PUT /api/projects/1/ - оновити повністю
    PATCH /api/projects/1/ - оновити частково
    DELETE /api/projects/1/ - видалити
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


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
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    
    def get_queryset(self):
        queryset = Place.objects.all()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset