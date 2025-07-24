from rest_framework import serializers
from .models import *


class hora_parqueoSerializer(serializers.ModelSerializer):

    class Meta:
        model = hora_parqueo
        fields = ('__all__')