from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    TestObjSerializer, GroupSerializer, DocumentSerializer
)

from .models import TestObj, Group, Document


class CurrentUserView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class TestObjViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TestObj.objects.all()
    serializer_class = TestObjSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
