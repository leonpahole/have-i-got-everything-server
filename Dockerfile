FROM python:3-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev

RUN pip install -U pipenv

RUN pip install uwsgi

RUN mkdir /code

WORKDIR /code

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY . .

EXPOSE 8000

CMD ["uwsgi", "--http", ":8000", "--ini", "/code/hige.uwsgi.ini"]
