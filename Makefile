.PHONY: up test
up:
	docker compose up -d

test:
	pytest -q
