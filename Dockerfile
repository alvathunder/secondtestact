FROM ubuntu:latest

RUN sudo apt install python3 py3-pip

CMD python3 --version

RUN sudo apt install bash-completion

ENV PORT 8080

EXPOSE $PORT

COPY . . 

WORKDIR /app

USER root

RUN sudo chmod +x scripts.sh

ENTRYPOINT ["sh", "./scripts.sh]

#ENTRYPOINT ["python", "steve.py"]






# ENTRYPOINT ["sh","/app/script.sh"]





