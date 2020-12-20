from django.shortcuts import render
from rest_framework import viewsets
from .models import Board, Tusk
from .serializers import BoardSerializer, TuskSerializer


class BoardView(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class TuskView(viewsets.ModelViewSet):
    queryset = Tusk.objects.all()
    serializer_class = TuskSerializer
