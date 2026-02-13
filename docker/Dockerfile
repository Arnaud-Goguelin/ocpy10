
# Build stage
FROM python:3.13-alpine AS build-stage

WORKDIR /usr/src/app

# Install build dependencies
RUN apk add --no-cache --update gcc libc-dev

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install Python dependencies in a virtual environment
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

# Runtime stage
FROM python:3.13-alpine

WORKDIR /usr/src/app

# Environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE=config.settings

RUN adduser --system --no-create-home nonroot

# Copy UV and virtual environment from build stage
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY --from=build-stage /usr/src/app/.venv /usr/src/app/.venv

# set PATH as env variable in order to allow python commands in docker without rewrite path
ENV PATH="/usr/src/app/.venv/bin:$PATH"

# Copy the application code
COPY . .

# Copy and set permissions for entrypoint script
COPY docker/entrypoint.sh /usr/local/bin/
COPY docker/scheduler.sh /usr/local/bin/
# correct endline in LF
RUN dos2unix /usr/local/bin/entrypoint.sh /usr/local/bin/scheduler.sh || sed -i 's/\r$//' /usr/local/bin/entrypoint.sh /usr/local/bin/scheduler.sh \
    # set permissions for nonroot user: only read and execute\
    && chown nonroot /usr/local/bin/entrypoint.sh /usr/local/bin/scheduler.sh \
    && chmod 500 /usr/local/bin/entrypoint.sh /usr/local/bin/scheduler.sh

USER nonroot

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
