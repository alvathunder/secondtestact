FROM ubuntu:latest

USER root

RUN apt update && apt upgrade

RUN apt install python3

CMD python3 --version

RUN apt install bash-completion

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

RUN sudo chmod +x scripts.sh

ENTRYPOINT ["sh", "./scripts.sh]

#ENTRYPOINT ["python", "steve.py"]

# ENTRYPOINT ["sh","/app/script.sh"]





