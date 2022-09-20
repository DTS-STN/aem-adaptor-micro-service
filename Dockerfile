FROM python:3.9-slim-bullseye

ARG user=habetrot
ARG home=/home/$user
ARG group=habetrot
RUN addgroup $group
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home $home \
    --ingroup $group \
    $user

RUN mkdir /app && chown $user:$user /app

WORKDIR /app

USER $user

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1

COPY . .

RUN python3 -m pip install --user pipx && python3 -m pipx ensurepath

ENV PATH /home/habetrot/.local/bin:$PATH
 
RUN pipx install poetry && poetry install --no-interaction --no-ansi --only main

EXPOSE 8000

CMD [ "poetry", "run", "start" ]
