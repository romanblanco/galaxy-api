from django.db import transaction

from rest_framework.serializers import ModelSerializer

from galaxy_api.api import models
from galaxy_api.auth import models as auth_models

class GroupSerializer(ModelSerializer):
    class Meta:
        model = auth_models.Group
        fields = ('name',)
