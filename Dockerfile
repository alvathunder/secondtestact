FROM ubuntu:latest

USER root

RUN apt update && apt upgrade

RUN apt install apt-utils

RUN apt install python3 -y

CMD python3 --version

RUN apt install bash-completion

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

RUN chmod +x scripts.sh

ENTRYPOINT ["./scripts.sh"]

#ENTRYPOINT ["python", "steve.py"]

# ENTRYPOINT ["sh","/app/script.sh"]





