# FindTeam

## Запуск бота (онбординг)

1. **PostgreSQL** — создайте БД и задайте URI для async SQLAlchemy, например:

   `postgresql+asyncpg://USER:PASSWORD@localhost:5432/findteam`

2. **Переменные окружения** (в шелле или в `.env`, который вы подгружаете сами):

   - `DB_URI` — строка подключения выше  
   - `TELEGRAM_BOT_TOKEN` — токен бота от [@BotFather](https://t.me/BotFather)

3. **Миграции** (из корня репозитория):

   ```bash
   uv sync
   export DB_URI='postgresql+asyncpg://...'
   uv run alembic upgrade head
   ```

4. **Старт бота**:

   ```bash
   export DB_URI='postgresql+asyncpg://...'
   export TELEGRAM_BOT_TOKEN='...'
   uv run findteam-bot
   ```

   Либо: `uv run python -m src.main` (нужен установленный пакет `uv sync` или `PYTHONPATH=.`).

В Telegram: команда `/start` — регистрация по шагам; в конце кнопка «Завершить регистрацию».
