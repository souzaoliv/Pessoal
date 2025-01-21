FROM python:3.13.1-slim-bullseye

WORKDIR /app

COPY . . 

RUN pip3 install -r requirements/dev.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
