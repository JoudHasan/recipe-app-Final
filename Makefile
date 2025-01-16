# Set Python executable
PYTHON := python3

# Default target
all:
	@echo "Please specify a target. Options: dev-start, dev-migrate, prod-install, prod-gunicorn, etc."

# Development Commands
dev-start:
	$(PYTHON) manage.py runserver --settings=config.settings.dev

dev-startapp:
	@if [ -z "$(app)" ]; then echo "Error: app variable not set. Use: make dev-startapp app=app_name"; exit 1; fi
	cd apps && $(PYTHON) ../manage.py startapp $(app) --settings=config.settings.dev

dev-migrate:
	$(PYTHON) manage.py migrate --settings=config.settings.dev

dev-makemigrations:
	$(PYTHON) manage.py makemigrations --settings=config.settings.dev

dev-dbshell:
	$(PYTHON) manage.py dbshell --settings=config.settings.dev

dev-shell:
	$(PYTHON) manage.py shell --settings=config.settings.dev

dev-shell-plus:
	$(PYTHON) manage.py shell_plus --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-test:
	$(PYTHON) manage.py test --settings=config.settings.dev

# Production Commands
prod-collectstatic:
	$(PYTHON) manage.py collectstatic --noinput --settings=config.settings.prod

prod-install:
	pip install -r requirements/prod.txt

prod-migrate:
	$(PYTHON) manage.py migrate --settings=config.settings.prod

prod-gunicorn:
	gunicorn config.wsgi:application \
		--env DJANGO_SETTINGS_MODULE=config.settings.prod \
		--bind 0.0.0.0:8000 \
		--log-file -
