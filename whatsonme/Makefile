start:
	# docker-compose up --build -d
	docker-compose up --build

stop:
	docker-compose down

restart: | stop start

superuser: 
	docker-compose down
	docker-compose run web python /code/manage.py createsuperuser
	docker-compose down

# how to check if the container running its ok if not start it before / also how to open a new terminal if we start first the n exec it still on the same terminal 
db:
	docker-compose up -d db
	docker-compose exec db psql whatsonme awsahmed

shell: # Access the Django Shell on the container
	docker-compose exec web ./manage.py shell

make_migrations:
	docker-compose exec web ./manage.py makemigrations

migrate:
	docker-compose exec web ./manage.py migrate

.PHONY: start stop restart superuser db shell