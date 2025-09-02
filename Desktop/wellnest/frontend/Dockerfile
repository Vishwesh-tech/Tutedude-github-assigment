FROM python:3.8-slim-buster

ENV BACKEND_URL=http://localhost:9500 

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD ["app.py"]