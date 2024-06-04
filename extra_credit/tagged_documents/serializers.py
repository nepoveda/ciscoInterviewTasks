from rest_framework import serializers

from tagged_documents.models import Document, Tagg


class TaggSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagg
        fields = ["pk", "slug"]


class DocumentSerializer(serializers.ModelSerializer):
    tags = TaggSerializer(many=True)

    class Meta:
        model = Document
        fields = ["pk", "doc", "tags"]
