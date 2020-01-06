from rest_framework import mixins
from rest_framework import viewsets
from galaxy_api.auth import models as auth_models
from galaxy_api.api.ui import serializers

class GroupViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "name"
    fields = '__all__'

    def get_serializer_class(self):
        return serializers.GroupSerializer

    def get_queryset(self):
        return auth_models.Group.objects.all()
