up:
	pipenv install
	docker compose up -d
	pipenv shell
	
start:
	python manage.py runserver
	
migrate:
	python manage.py migrate
	
make-migration:
	python manage.py makemigrations hige