FROM python:3.8-slim

ADD . /app
RUN pip install /app
RUN rm -drf /app
RUN mkdir /workspace
WORKDIR /workspace

ENTRYPOINT [ "snipeit-to-qr" ]
