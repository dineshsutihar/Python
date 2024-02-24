# HTTP Status Codes

|-------------|-------------|
| Status Code | Description |
|-------------|-------------|
| 200         | OK          |
| 201         | Created     |
| 301         | Moved Permanently |
| 403         | Forbidden   |
| 404         | Not Found   |
| 500         | Internal Server Error |
| 503         | Service Unavailable |
| 504         | Gateway Timeout |
| 505         | HTTP Version Not Supported |
| 507         | Insufficient Storage |
| 511         | Network Authentication Required |


# HTTP Methods

|-------------|-------------|
| Method      | Description |
|-------------|-------------|
| GET         | Retrieve data |
| POST        | Submit data |
| PUT         | Update data |
| DELETE      | Delete data |
| OPTIONS     | Get information about the communication options |
| HEAD        | Get the header information |
| TRACE       | Get the information about the path of the communication |
| CONNECT     | Establish a tunnel to the server |
| PATCH       | Update partial data |
|-------------|-------------|

# HTTP Headers

|-------------|-------------|
| Header      | Description |
|-------------|-------------|
| Accept      | The media type that is accepted by the client |
| Accept-Charset | The character sets that are accepted by the client |
| Accept-Encoding | The encoding that is accepted by the client |
| Accept-Language | The language that is accepted by the client |
| Authorization | The credentials that are required for the client to access the server |
| Cache-Control | The directives that are required for the client to access the server |
| Connection  | The options that are required for the client to access the server |
| Content-Length | The length of the content |
| Content-Type | The media type of the content |
| Cookie      | The cookie that is required for the client to access the server |
| Date        | The date and time of the request |
| Host        | The domain name of the server |
| If-Match    | The entity tag that is required for the client to access the server |
| If-Modified-Since | The date and time that is required for the client to access the server |
| If-None-Match | The entity tag that is required for the client to access the server |
| If-Range    | The entity tag that is required for the client to access the server |
| If-Unmodified-Since | The date and time that is required for the client to access the server |
| Max-Forwards | The maximum number of times that the request can be forwarded |


# Django create a new project

```bash
django-admin startproject project_name
```

After creating the project, you can see the following files and directories:

```bash
project_name/
    manage.py
    project_name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Use of each file and directory:

- `manage.py`: used to manage the project and perform tasks such as creating a new application, running the development server, and running tests.
- `project_name/`: the directory that contains the project.
- `__init__.py`: an empty file that tells Python that this directory should be considered a Python package.
- `settings.py`: contains the settings for the project.
- `urls.py`: contains the URL patterns for the project.
- `asgi.py`: an entry point for ASGI-compatible web servers to serve the project.
- `wsgi.py`: an entry point for WSGI-compatible web servers to serve the project.
- `db.sqlite3`: the default database for the project.

## Run the development server

```bash   
python manage.py runserver
```

## Create a new application
### Why create a new application? and what is an application? in Django?..
- An application is a web application that does something – e.g., a weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
- Eg: Google has a project called "Google Search" and it has multiple applications like "Google Maps", "Google Images", "Google News", etc.

### How to create a new application?
```bash
python manage.py startapp app_name
```
- Now we have created a new application, you can see the following files and directories:
```bash
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Use of each file and directory:

- `__init__.py`: an empty file that tells Python that this directory should be considered a Python package.
- `admin.py`: used to register the models of the application with the Django admin application.
- `apps.py`: contains the configuration of the application.
- `migrations/`: contains the database migrations for the application.
- `models.py`: contains the models of the application.
- `tests.py`: contains the tests for the application.
- `views.py`: contains the views of the application.

### Add the application to INSTALLED_APPS
1.  To add the application to the project, you need to add the application to the `INSTALLED_APPS` list in the `settings.py` file of the project.

```python
INSTALLED_APPS = [
    'app_name', # add the application to the INSTALLED_APPS list
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
2. Now you need to create a URL pattern for the application in the `urls.py` file of the project.

```python
from django.urls import include

urlpatterns = [
    path('app_name/', include('app_name.urls')), # add the URL pattern for the application
    path('admin/', admin.site.urls),
]
```
3. Now you need to create a URL pattern for the application in the `urls.py` file of the application.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # add the URL pattern for the application
]
```
4. Now you need to create a view for the application in the `views.py` file of the application.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the app_name index.")
```


