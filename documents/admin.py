from django.contrib import admin

from .models import Category, Document
from .forms import CategoryForm, DocumentForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    date_hierarchy = 'created'
    form = CategoryForm


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    date_hierarchy = 'created'
    form = DocumentForm

    def save_model(self, request, obj, form, change):
        if request.FILES['document']:
            for f in request.FILES.getlist('document'):
                obj.pk = None
                filename = f.name.split('.')[0]
                obj.name = filename
                obj.document = f
                obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
