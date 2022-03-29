# Dockerfile for ride matching consumer
FROM python:3.7

# install pika to access rabbitmq
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /home/pes1ug19cs077/CloudHack_2/app/consumer

# copy the file
COPY Dockerfile .

# start command
CMD [ "python", "Dockerfile.py" ]
