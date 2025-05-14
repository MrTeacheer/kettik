backend = python src/manage.py

run:
	@$(backend) runserver 8001

migrate:
	@$(backend) makemigrations
	@$(backend) migrate

superuser:
	@$(backend) createsuperuser

del-migr:
	@find src/ -type f -path "*/migrations/0*" -delete

static:
	@$(backend) collectstatic
