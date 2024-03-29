FROM python:3.9-slim-buster

WORKDIR /myportfolio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

COPY . .

EXPOSE 5000