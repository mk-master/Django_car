FROM python:3.12-bookworm

WORKDIR /app

RUN pip install --upgrade pip "poetry==2.3.2"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

RUN chmod +x ./prestart.sh

ENTRYPOINT ["./prestart.sh"]