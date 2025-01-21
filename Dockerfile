FROM python:3.13.1-slim-bullseye

WORKDIR /app

COPY . . 

RUN pip3 install -r requirements/prod.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoapp.wsgi:application"]

