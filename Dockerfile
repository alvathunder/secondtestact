FROM python:3.8

RUN apk add --no-cache python3 py3-pip

EXPOSE 8080

COPY . . 
WORKDIR ./steve.py

ENTRYPOINT ["python", "steve.py"]

