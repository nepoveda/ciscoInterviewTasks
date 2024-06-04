from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from tagged_documents.models import Document, Tagg
from tagged_documents.serializers import DocumentSerializer


# Create your views here.
class DocumentList(ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        tag = self.request.query_params.get("tag")
        tag = Tagg.objects.filter(slug=tag).first()
        if tag:
            return Document.objects.filter(
                Q(tags__in=[tag.pk]) | Q(tags__parent=tag.pk)
            )
        return Document.objects.all()
