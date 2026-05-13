## 🛠 Гайд по использованию Pixi
### 1. Установка pixi
   **Windows:**  `iwr -useb https://pixi.sh/install.ps1 | iex`
   **macOS/Linux:** curl -fsSL https://pixi.sh/install.sh | bash

### 2. Настройка окружения
В корне проекта выполните:
`pixi install` -- установка общих зависимостей

При работе с конкретным модулем исползуйте соответствующие окружения
**etl-env** - для ETL-инстурмента
**front-env** - для API/frontend части
**llm-env** - для части ассистента

### 3. Работа в терминале
Для загрузки завсисимостей: 
`pixi install -e   ...-env`

Для инициализации окружения (как в .env):
`pixi shell -e   ...-env`

Быстрый запуск без входа: `pixi run -e <имя-env> python <скрипт>.py`

Для добавления новых зависимостей:
`pixi add --feature (название соотв. окр.) ...(название библиотеки/фреймворка)`
*Если ошибка то* `pixi add --feature (название соотв. окр.) -pypi ...`

!!!Обязательно в IDE указать интерпретатор Python !!!

**Windows:** `.pixi/envs/<имя-env>/python.exe`
**macOS/Linux:** `.pixi/envs/<имя-env>/bin/python`





