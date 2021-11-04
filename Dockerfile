FROM python:3.8

WORKDIR /app
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y make python3-pip python3-dev libffi-dev libssl-dev

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]