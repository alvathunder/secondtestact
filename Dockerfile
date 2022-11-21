FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

CMD python3 --version

EXPOSE 8080

COPY . . 

WORKDIR /app

ENTRYPOINT ["sudo","npm", "start"]

#ENTRYPOINT ["python", "steve.py"]




