FROM python:3.10.6-slim-buster as base
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN pip3 install -e .

CMD ["flask", "run", "--host=0.0.0.0"]
