FROM python:3.9.2-buster
LABEL author="lewin.kaestner@uni-potsdam.de"

WORKDIR /code

COPY scrapyd.conf /etc/scrapyd/scrapyd.conf

# Copy the dependencies to the container and install the python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

COPY src/ /code/

EXPOSE 6800
ENTRYPOINT "/usr/local/bin/scrapyd"
