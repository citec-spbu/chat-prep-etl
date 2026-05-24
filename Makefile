PROJECT_NAME = chat_prep_etl
DOCKER_RUNTIME ?= docker
etl-service_URL ?= http://localhost:8067/docs
tesiting-system_URL ?= http://localhost:8881/docs
SERVICE ?=
URL ?= http://localhost:8881/docs"

.PHONY: help build up down logs open

help:   ## Показать справку
	@echo "Доступные цели:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

build:  ## Собрать образы
	$(DOCKER_RUNTIME) compose build 

up:     ## Запустить сервисы (все, если SERVICE не задан)
	@if [ -z "$(SERVICE)" ]; then \
		echo "Запуск всех сервисов..."; \
		$(DOCKER_RUNTIME) compose up -d; \
	else \
		echo "Запуск сервиса $(SERVICE)..."; \
		$(DOCKER_RUNTIME) compose up -d $(SERVICE); \
	fi

down:   ## Остановить сервисы (все, если SERVICE не задан)
	@if [ -z "$(SERVICE)" ]; then \
		echo "Остановка всех сервисов..."; \
		$(DOCKER_RUNTIME) compose down -v; \
	else \
		echo "Остановка сервиса $(SERVICE)..."; \
		$(DOCKER_RUNTIME) compose stop $(SERVICE); \
		echo "Чтобы удалить контейнер, выполните: docker compose rm $(SERVICE)"; \
	fi

logs:   ## Показать логи (по умолчанию все, или SERVICE=...). Для выхода Ctrl+C.
	@if [ -z "$(SERVICE)" ]; then \
		$(DOCKER_RUNTIME) compose logs -f; \
	else \
		$(DOCKER_RUNTIME) compose logs -f $(SERVICE); \
	fi

open:   ## Открыть URL в браузере, не блокируя терминал. Пример: make open URL=http://localhost:8000
	@if [ -z "$(URL)" ]; then \
		$(URL) ?= http://localhost:8881"; \
	fi
	@echo "Открываем $(URL) в браузере..."
	@case "$$(uname -s)" in \
		Darwin*)  open "$(URL)" & ;; \
		Linux*)   (xdg-open "$(URL)" &> /dev/null &) ;; \
		MINGW*)   start "$(URL)" & ;; \
		CYGWIN*)  start "$(URL)" & ;; \
		*)        echo "Не удалось определить команду для открытия браузера"; exit 1 ;; \
	esac
	@echo "Done."

# Вспомогательная цель для вывода справки без аргументов
default: help
