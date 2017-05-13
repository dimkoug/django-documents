from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from djpjax import PJAXResponseMixin

from .models import Category, Document

from .forms import CategoryForm, DocumentForm


class CategoryList(PJAXResponseMixin, ListView):
    model = Category
    pjax_template_name = "category_list.html"


class CategoryDetail(PJAXResponseMixin, DetailView):

    model = Category
    pjax_template_name = "category_detail.html"


class CategoryCreate(PJAXResponseMixin, CreateView):
    model = Category
    form_class = CategoryForm
    pjax_template_name = "category_form.html"

    def form_valid(self, form):
        return super(CategoryCreate, self).form_valid(form)


class CategoryUpdate(PJAXResponseMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_update_form'
    pjax_template_name = "category_update_form.html"


class CategoryDelete(PJAXResponseMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('documents:category.list')
    pjax_template_name = "category_confirm_delete.html"


class DocumentList(PJAXResponseMixin, ListView):
    model = Document
    pjax_template_name = "document_list.html"


class DocumentDetail(PJAXResponseMixin, DetailView):

    model = Document
    pjax_template_name = "document_detail.html"


class DocumentCreate(PJAXResponseMixin, CreateView):
    model = Document
    form_class = DocumentForm
    pjax_template_name = "document_form.html"

    def form_valid(self, form):
        new_file = form.save(commit=False)
        if self.request.FILES['document']:
            for f in self.request.FILES.getlist('document'):
                new_file.pk = None
                new_file.name = f.name
                new_file.document = f
                new_file.save()
        return super(DocumentCreate, self).form_valid(form)


class DocumentUpdate(PJAXResponseMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    template_name_suffix = '_update_form'
    pjax_template_name = "document_update_form.html"


class DocumentDelete(PJAXResponseMixin, DeleteView):
    model = Document
    success_url = reverse_lazy('documents:document.list')
    pjax_template_name = "document_confirm_delete.html"
