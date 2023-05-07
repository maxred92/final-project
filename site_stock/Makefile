FORMAT_FOLDER?=.
format:
	python -m isort ${FORMAT_FOLDER}
	python -m black ${FORMAT_FOLDER}
	python -m flake8 ${FORMAT_FOLDER}
freeze:
	pip freeze > requirements.txt
install:
	pip install -r requirements.txt
run:
	python manage.py runserver
