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

ENV PIPENV_IGNORE_VIRTUALENVS=1 

COPY Pipfile .
COPY Pipfile.lock .
COPY app app

RUN mkdir .venv && python3 -m pip install --user pipx && python3 -m pipx ensurepath

ENV PATH /home/habetrot/.local/bin:$PATH
 
RUN pipx install pipenv && pipenv install 

EXPOSE 8000

CMD [ "pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
