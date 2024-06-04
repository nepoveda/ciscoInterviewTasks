from django.db import models


# Create your models here.
class Tagg(models.Model):
    slug = models.SlugField(allow_unicode=False)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="sub_tags"
    )

    def __str__(self):
        return self.slug


class Document(models.Model):
    doc = models.FileField(upload_to="documents/")
    tags = models.ManyToManyField(Tagg, blank=True)
