backend = python src/manage.py

up:
	@sudo docker compose -f .devops/backend.yaml up --build
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
