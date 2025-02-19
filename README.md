# Django API Template

This is a Django API template that can be used to quickly start a new project. It includes a few basic features that are commonly used in most projects.

In order to have your project up-and-running right away, just follow the [backend setup](backend/README.md#setup) and then the [project setup](#setup)

The template includes the following:

* [Backend / API](#backend-api)
* [Nginx](#nginx)
* [Docker / Docker-compose](#docker-docker_compose)
* [Setup](#setup)
* [Useful commands](#useful-commands)


## Backend / API <a name="backend-api"></a>
This template includes a Django project that can be used to create a RESTful API. You can use this project to create your own API endpoints and serve data to your frontend application.

A basic structure is already set up, with a few example models, serializers, views and urls. You can use this structure to get started quickly and build your project on top of it.

More details can be found in the [backend README](backend/README.md).


## Nginx <a name="nginx"></a>
This template includes an Nginx configuration file that can be used to serve your Django API project. You can use this file to configure Nginx to serve your project, but a basic configuration is already included so you can get started quickly.

The basic Nginx configuration will route all requests made to `/api/` and `/admin/` to the backend application, and will serve all static and media files directly from the filesystem (through the `static` and `media` directories inside the django application).


## Docker / Docker-compose <a name="docker-docker_compose"></a>
This template includes a `docker-compose.yaml` and a `docker-compose.prod.yaml` files that can be used to run your project in a Docker container.

You can run the project in development mode using the `docker-compose.yaml` file, which will start only the Django application and using the development server.

You can also run the project in production mode using the `docker-compose.prod.yaml` file, which will start the Django application (using gunicorn as the WSGI server), Nginx (to act as a reverse-proxy and load-balancer if needed) and a PostgreSQL database. This will allow you to run your project in a production-like environment, with all the services running in separate containers.


## Setup <a name="setup"></a>
To set up the project, just follow the steps documented in the [backend README](backend/README.md) and then you can build and run the backend application using the following commands:

```bash
docker-compose up --build
```

or to run the project in production mode:

```bash
docker-compose -f docker-compose.prod.yaml up --build
```

This will start the Django application (and Nginx and PostgreSQL services, if production mode), and you can access the API at `http://localhost:8080/api/` and the Django admin at `http://localhost:8080/admin/`.


## Useful commands <a name="useful-commands"></a>

- To run the Django development server and ssh into the container:

```bash
docker-compose run --build --service-ports backend bash
```
