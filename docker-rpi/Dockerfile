FROM resin/rpi-raspbian:wheezy

RUN apt-get update && apt-get install -y \
	python2.7 python-dev python-pip

RUN pip install paho-mqtt

COPY . /app
CMD ["python", "/app/mqtt_producer.py"]

