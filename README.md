# Work card demo
Backend REST api for demostrating Django and Django Rest Framework capabilities

## Core libs and DB
1. [Django](https://www.djangoproject.com/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)

All requirements you can find in `Pipfile`


## Getting started
### To run locally
Use [pipenv](https://github.com/pypa/pipenv)

```sh
$ pipenv shell
$ pipenv install
```
Go to src directory and run

```sh
$ python manage.py migrate
$ python manage.py test
$ python manage.py runserver
```

Open `http://localhost:8000` to view it in the browser

## [Django admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) web interface (user should be `is_staff` od `is_superuser`)
`http://localhost:8000/admin`


## [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/)
`http://localhost:8000/api/v1/`


## Swagger and Redoc
`http://localhost:8000/api/docs/schema/swagger-ui/`
`http://localhost:8000/api/docs/schema/redoc/`

## YAML schema
`http://localhost:8000/api/docs/schema/`

Use your user credentials to login into the swagger
