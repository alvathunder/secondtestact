FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

CMD python3 --version

EXPOSE 8080

COPY . . 

WORKDIR ./steve.py

ENTRYPOINT ["python", "steve.py"]




