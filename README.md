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

