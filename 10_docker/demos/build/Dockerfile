FROM ubuntu:20.04
COPY . /app
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip install -r /app/requirements.txt
EXPOSE 8080
CMD python /app/app.py
