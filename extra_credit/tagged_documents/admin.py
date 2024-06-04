from django.contrib import admin

from tagged_documents.models import Document, Tagg

# Register your models here.
admin.site.register(Document)
admin.site.register(Tagg)
