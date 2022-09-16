FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY *.py /app/.
COPY api /app/api
COPY model /app/model
COPY repository /app/repository
COPY service /app/service
COPY util /app/util

RUN pip install --upgrade pip setuptools==57.5.0
RUN pip install ez_setup
RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]