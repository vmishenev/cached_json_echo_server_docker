FROM python:3

RUN pip3 install redis
COPY ./server.py /

EXPOSE 9091
ENTRYPOINT ["python", "server.py"]
