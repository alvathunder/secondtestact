FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

CMD python3 --version

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

USER root

RUN chmod +x script.sh

ENTRYPOINT ["sh", "./script.sh]

#ENTRYPOINT ["python", "steve.py"]






# ENTRYPOINT ["sh","/app/script.sh"]





