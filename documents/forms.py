from django import forms

from .models import Category, Document


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class DocumentForm(forms.ModelForm):
    document = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(DocumentForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['document'].widget.attrs['multiple'] = False

    class Meta:
        model = Document
        fields = ['category', 'document']
