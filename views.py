from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_datatables.filters import DatatablesFilterBackend
from .models import Profile
from .filters import ProfileFilter
from .serializers import ProfileSerializer


class ProfileView(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = ProfileSerializer
    all_fields = [f.name for f in Profile._meta.get_fields()]
    filter_backends = [
        DjangoFilterBackend,
        DatatablesFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = ProfileFilter
    search_fields = all_fields

    def get_queryset(self):
        queryset = Profile.objects.filter()
        return queryset
