from django import forms

from .models import Category, Document


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ['name']


class DocumentForm(forms.ModelForm):
    document = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-control'
        if self.instance.pk:
            self.fields['document'].widget.attrs['multiple'] = False

    class Meta:
        model = Document
        fields = ['category', 'document']
