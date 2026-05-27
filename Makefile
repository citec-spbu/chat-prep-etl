PROJECT_NAME = chat_prep_etl
DOCKER_RUNTIME ?= docker
SERVICE ?=

#обработка конфига для определнения портов и доп контейнера для локального инференса
#образ yq - легковесный, около 10MB 
YQ = docker run --rm -v "$(CURDIR):/work" -w /work mikefarah/yq
TESTING_SYSTEM_PORT := $(shell $(YQ) '.testing_system.port // 8501' config/config.yaml 2>/dev/null)
ASSISTANTS_TYPE    := $(shell $(YQ) '.testing_system.assistants.type // "cloud"' config/config.yaml 2>/dev/null)
OLLAMA_PORT        := $(shell $(YQ) '.testing_system.assistants.ollama.port // 11434' config/config.yaml 2>/dev/null)
ETL_PORT        := $(shell $(YQ) '.etl.port // 8067' config/config.yaml 2>/dev/null)
FRONTEND_PORT        := $(shell $(YQ) '.frontend.port // 8501' config/config.yaml 2>/dev/null)
OLLAMA_ENABLED := $(if $(filter ollama,$(ASSISTANTS_TYPE)),true,false)

export TESTING_SYSTEM_PORT
export OLLAMA_PORT
export ETL_PORT
export FRONTEND_PORT
export ASSISTANTS_TYPE


.PHONY: help build up down logs open

help:   ## Показать справку
	@echo "Доступные цели:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

build:  ## Собрать образы
	@if [ -z "$(SERVICE)" ]; then \
		$(DOCKER_RUNTIME) compose build; \
	else \
		$(DOCKER_RUNTIME) compose build $(SERVICE); \
	fi

up:     ## Запустить сервисы (автоматически определяет, нужна ли Ollama)
	@if [ -z "$(SERVICE)" ]; then \
		if [ "$(ASSISTANTS_TYPE)" = "ollama" ]; then \
			echo "Запуск ВСЕХ сервисов с локальной Ollama (тип=ollama)"; \
			TESTING_SYSTEM_PORT=$(TESTING_SYSTEM_PORT) OLLAMA_PORT=$(OLLAMA_PORT) \
			$(DOCKER_RUNTIME) compose --profile ollama up -d; \
		else \
			echo "Запуск ВСЕХ сервисов без Ollama (тип=cloud)"; \
			TESTING_SYSTEM_PORT=$(TESTING_SYSTEM_PORT) \
			$(DOCKER_RUNTIME) compose up -d; \
		fi \
	elif [ "$(SERVICE)" = "testing-system" ]; then \
		if [ "$(ASSISTANTS_TYPE)" = "ollama" ]; then \
			echo "Запуск только testing-system + Ollama (тип=ollama)"; \
			TESTING_SYSTEM_PORT=$(TESTING_SYSTEM_PORT) OLLAMA_PORT=$(OLLAMA_PORT) \
			$(DOCKER_RUNTIME) compose --profile ollama up -d $(SERVICE); \
		else \
			echo "Запуск только testing-system без Ollama (тип=cloud)"; \
			TESTING_SYSTEM_PORT=$(TESTING_SYSTEM_PORT) \
			$(DOCKER_RUNTIME) compose up -d $(SERVICE); \
		fi \
	else \
		echo "Запуск сервиса $(SERVICE)"; \
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

logs:   ## Показать логи (по умолчанию все, или SERVICE=...)
	@if [ -z "$(SERVICE)" ]; then \
		$(DOCKER_RUNTIME) compose logs -f; \
	else \
		$(DOCKER_RUNTIME) compose logs -f $(SERVICE); \
	fi

default: help
