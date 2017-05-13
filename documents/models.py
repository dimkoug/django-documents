from django.db import models
from django.urls import reverse


class Timestammped(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        abstract = True


class Category(Timestammped):
    name = models.CharField(max_length=255)

    class Meta:
        default_related_name = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('documents:category.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Document(Timestammped):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')

    class Meta:
        default_related_name = 'documents'
        verbose_name = 'document'
        verbose_name_plural = 'documents'

    def get_absolute_url(self):
        return reverse('documents:document.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
