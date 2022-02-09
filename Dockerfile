FROM python:3.9-alpine3.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/app
ENV MUSL_LOCPATH="/usr/share/i18n/locales/musl"

RUN apk add --no-cache \
    curl `# для установки poetry` \
    gcc `# для установки poetry` \
    libffi-dev `# для установки poetry` \
    git `# для установки зависимостей из git` \
    build-base  `# для сборки пакетов` \
    musl-locales musl-locales-lang `# для работы русской локали в python` \
    librdkafka-dev `# для работы confluent-kafka`

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN mkdir /app
COPY pyproject.toml /app/
WORKDIR /app/
RUN poetry install
COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for
COPY / /app/
RUN chmod +x entrypoint.sh