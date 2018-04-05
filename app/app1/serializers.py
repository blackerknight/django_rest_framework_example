from rest_framework import serializers
from app.app1.models import Model1

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = ('id', 'name')
