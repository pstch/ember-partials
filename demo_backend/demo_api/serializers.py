from rest_framework import serializers

from django.contrib.auth.models import User

from .models import TestObj, Group, Document


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined'
        )


class TestObjSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestObj
        fields = ('id', 'name', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'documents')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id', 'name', 'group', 'number',
            'description', 'progress', 'files'
        )
