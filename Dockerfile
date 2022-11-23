FROM ubuntu:latest

USER root

RUN apt update && apt upgrade

RUN apt install apt-utils

RUN apt install python3 -y

CMD python3 --version

RUN apt install bash-completion

RUN apt install curl -y

RUN apt install zip -y

RUN apt install unzip -y

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

RUN echo exit 101 | sudo tee /usr/sbin/policy-rc.d

RUN chmod +x scripts.sh

ENTRYPOINT ["bash","./scripts.sh"]

#ENTRYPOINT ["python", "steve.py"]

# ENTRYPOINT ["sh","/app/script.sh"]





