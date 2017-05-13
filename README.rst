=====
Documents
=====

Upload multiple documents


Installation
------------

    ::

      pip install -e https://github.com/dimkoug/django-documents.git#egg=documents


Quick start
-----------

1. Add "documents" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'documents',
    ]

2. Include the documents URLconf in your project urls.py like this::

    url(r'^documents/', include('documents.urls', namespace='documents')),

3. Run `python manage.py migrate` to create the documents models.

4. Start the development server and visit http://127.0.0.1:8000/documents/
   to upload documents.

5. Visit http://127.0.0.1:8000/documents/.

Dependencies
------------

::

  https://github.com/eventials/django-pjax
  https://github.com/defunkt/jquery-pjax.git
