from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Project, ProjectCategory, Link,\
    LinkCategory, Image, TaggedProject

from taggit.models import Tag

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

class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    thumbnailBW = serializers.ImageField(read_only=True)
    class Meta:
        model = Image

class ProjectTagSerializer(serializers.ModelSerializer, ):
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedProject
        fields = ('tag_id', 'tag')
