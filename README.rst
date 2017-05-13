=====
Documents
=====

Upload multiple documents

Quick start
-----------

1. Add "documents" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'documents',
    ]

2. Include the documents URLconf in your project urls.py like this::

    url(r'^documents/', include('documents.urls', namespace='doscuments')),

3. Run `python manage.py migrate` to create the documents models.

4. Start the development server and visit http://127.0.0.1:8000/documents/
   to upload documents.

5. Visit http://127.0.0.1:8000/documents/.
