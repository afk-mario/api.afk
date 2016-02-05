from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Project, ProjectCategory, Link, LinkCategory


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Project


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory

class LinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkCategory

class ProjectLinksSerializer(serializers.ModelSerializer):
    category = LinkCategorySerializer(read_only=True)
    class Meta:
        model = Link
