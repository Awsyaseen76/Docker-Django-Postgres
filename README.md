# THE FINAL STEPS TO RUN WHAT WE CREATE:
1. run the docker file from the directory containes the Dockerfile:
    `docker-compose up --build`
    it will reach to the point of running the server
    and run 2 containers: 
        - whatsonme_web_1
        - whatsonme_db_1
2. to create a superuser:
    -stop the containers:
        `docker-compose down`
    - create the superuser:
        `docker-compose run web python /code/manage.py createsuperuser`
        fill...
    then:
    `docker-compose up --build`
    will auto migrate and run the server



# ADD THE MAKE FILE ;)
if not available on the system:
`brew install make`

the available orders:

1. `make start`
    start the container 

2. `make stop`
    stop the container 

3. `make restart`
    restart the container

4. `make superuser`
    create the superuser for the project

5. `make db`
    connect to the database psql




# transfor the model data into API

### Using Django Rest Framework:
 - Serializer: transform the data into JSON

 1. add the `djangorestframework` to the Pipfile to install it.
    the problem is the Pipfile will install it but didn't update the Pipfile.lock
    to solve this but i think it is not the right way:
        insert this line in Dockerfile to install djangorestframework then the .lock file will be updated
        `RUN pipenv install djangorestframework`
 2. add `rest_framework` to the `INSTALLED_APPS` in settings.py
 3. create `serializers.py` file inside the app (auth_api)
 4. using Django RESTful Framework generic views instead of custom views and template because it is just API and they are pre-built views
 5. update `auth_api/views.py` to include generic views and create list_view and details_view
 6. the project's url point to the auth_api path
 7. update the app url 
 8. add

    
    1. install rest_framework





## Start from 0
1. Create environment: terminal
	`pipenv --python 3.7`
    `pipenv shell` enter the virtual environment
2. That will create Pipfile file containing:
		'''
            [[source]]
            name = "pypi"
            url = "https://pypi.org/simple"
            verify_ssl = true

            [dev-packages]

            [packages]

            [requires]
            python_version = "3.7"
        '''
3. add django to Pipfile under [requires]:
    django = "==2.2.0"
4. `pipenv install` that install the required packaches
5. Create django project:
    `django-admin startproject whatsonme`
6. ???????? not worked until:
    `pipenv install django`
7. migrate database the basic:
    `python manage.py migrate`
8. run the server:
    `python manage.py runserver`
9. Create the app: "auth_app"
    `python manage.py startapp auth_api`
    install `psycopg2` for database bindings to PostgreSQL

Put the project on Docker:
10. Change to postgres db:
11. change the settings to use the postgres:
    '''
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db', # will take from docker-compose.yml
            'PORT': 5432
        }
    }
    '''


....etc

