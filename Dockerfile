FROM python:3.9-slim-bullseye

ARG APP_HOST=0.0.0.0
ENV APP_HOST=${APP_HOST}
ARG APP_PORT=8000
ENV APP_PORT=${APP_PORT}
ARG APP_RELOAD=True
ENV APP_RELOAD=${APP_RELOAD}
ARG AEM_GRAPHQL_ENDPOINT
ENV AEM_GRAPHQL_ENDPOINT=${AEM_GRAPHQL_ENDPOINT}
ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}
ARG REDIS_HOST
ENV REDIS_HOST=${REDIS_HOST}
ARG REDIS_PORT
ENV REDIS_PORT=${REDIS_PORT}
ARG REDIS_DB
ENV REDIS_DB=${REDIS_DB}
ARG REDIS_USER
ENV REDIS_USER=${REDIS_USER}
ARG REDIS_PASSWORD
ENV REDIS_PASSWORD=${REDIS_PASSWORD}
ARG user=habetrot
ARG home=/home/$user
ARG group=habetrot

RUN addgroup $group && \
    adduser \
    --disabled-password \
    --gecos "" \
    --home $home \
    --ingroup $group \
    $user && \
    mkdir /app && \
    chown $user:$group /app

WORKDIR /app

USER $user

ENV POETRY_NO_INTERACTION=1

COPY pyproject.toml .
COPY --chown=$user:$group poetry.toml .
COPY poetry.lock .
COPY app app
COPY README.md .

RUN \
    python3 -m pip install --user pipx && \
    python3 -m pipx ensurepath

ENV PATH /home/habetrot/.local/bin:$PATH
 
RUN pipx install poetry && \
    poetry install --no-interaction --no-ansi --only main

EXPOSE $APP_PORT

CMD [ "poetry", "run", "start" ]
