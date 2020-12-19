default:
	@echo Please run any function

dbInit:
	source venv/bin/activate && python3
	# from app import db
	# db.create_all()
	# exit()

dev:
	@source venv/bin/activate && python3 run.py

build:
	@npm install --prefix client && \
	npm run build --prefix client

run:
	echo 'Ruuuuuun on port:${PORT}'; \
	gunicorn app:app -b '0.0.0.0:${PORT}'

freeze:
	pip3 freeze > requirements.txt

install:
	make build; \
	pip install -r requirements.txt; \
	virtualenv venv; \
	source venv/bin/activate; \
