# python-microservices

Source: <https://www.youtube.com/watch?v=0iB5IPoTDts>

## set up

```bash
    # Install
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support

    django-admin startproject admin

    # Run
    cd admin
    python3 manage.py runserver
```

## Adding dockerFiles

```bash
    # Docker
    docker-compose up
```

## Connect Django with MySQL with Docker

```bash
python manage.py startapp products
```

## Models & Serializers

- python manage.py makemigrations
- python manage.py migrate