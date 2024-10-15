from rest_framework import viewsets, permissions
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProgrammerSerializer