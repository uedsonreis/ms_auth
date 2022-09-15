FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools==57.5.0
RUN pip install ez_setup
RUN pip install -r requirements.txt

COPY *.py .
COPY api api
COPY model model
COPY repository repository
COPY service service
COPY util util

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]