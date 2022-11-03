from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from work_cards.models import WorkCard
from work_cards.serializers import WorkCardSerializer


class WorkCardViewSet(viewsets.ModelViewSet):
    """
    Work Card ViewSet [GET, POST, PUT, PATCH, DELETE]
    """

    serializer_class = WorkCardSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('contract_type', 'available_from', 'minimal_education_level', 'hours_per_week', 'branches', 'abroad')
    search_fields = ('looking_for', 'key_skills', 'current_client')

    def get_queryset(self):
        return WorkCard.objects.filter(user_id=self.request.user.id)
