from rest_framework import serializers
from .models import Board, Tusk

class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('id', 'title', 'created_at', 'modified_at')
        model = Board


class TuskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('id', 'title', 'created_at', 'modified_at', 'description', 'completed', 'board')
        model = Tusk