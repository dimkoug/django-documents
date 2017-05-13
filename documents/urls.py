from django.conf.urls import url

from .views import (
    DocumentList,
    DocumentCreate,
    DocumentUpdate,
    DocumentDelete,
    DocumentDetail,

    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    CategoryDetail,


)


urlpatterns = [
    url(
        r'^$',
        DocumentList.as_view(),
        name='document.list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        DocumentDetail.as_view(),
        name='document.detail'
    ),
    url(
        r'^add/$',
        DocumentCreate.as_view(),
        name='document.add'
    ),
    url(
        r'^(?P<pk>[0-9]+)/update/$',
        DocumentUpdate.as_view(),
        name='document.update'
    ),
    url(
        r'^(?P<pk>[0-9]+)/delete/$',
        DocumentDelete.as_view(),
        name='document.delete'
    ),
    url(
        r'^categories/$',
        CategoryList.as_view(),
        name='category.list'
    ),
    url(
        r'^category/(?P<pk>[0-9]+)/$',
        CategoryDetail.as_view(),
        name='category.detail'
    ),
    url(
        r'^category/add/$',
        CategoryCreate.as_view(),
        name='category.add'
    ),
    url(
        r'^category/(?P<pk>[0-9]+)/update/$',
        CategoryUpdate.as_view(),
        name='category.update'
    ),
    url(
        r'^category/(?P<pk>[0-9]+)/delete/$',
        CategoryDelete.as_view(),
        name='category.delete'
    ),
]
