FORMAT_FOLDER?=.
format:
	python -m isort ${FORMAT_FOLDER}
	python -m black ${FORMAT_FOLDER}
	python -m flake8 ${FORMAT_FOLDER}
freeze:
	pip freeze > requirements.txt
install:
	pip install -r requirements.txt
runserver:
	python manage.py runserver
makemigrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate