FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

CMD python3 --version

RUN apk add --no-cache --upgrade bash

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

USER root

RUN chmod +x scripts.sh

ENTRYPOINT ["sh", "./scripts.sh]

#ENTRYPOINT ["python", "steve.py"]






# ENTRYPOINT ["sh","/app/script.sh"]





