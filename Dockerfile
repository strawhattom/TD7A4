FROM python:3.10-alpine

ENV MONGO_URI=mongodb://mongodb:27017/testdb
WORKDIR /usr/src/app

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
