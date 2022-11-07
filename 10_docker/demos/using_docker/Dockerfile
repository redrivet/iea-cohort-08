FROM python:3.8-alpine

# TODO: Copy application files into container
COPY . /app

# TODO: Install required python libraries
RUN pip install -r /app/requirements.txt

# TODO: Have the container expose port 8080
EXPOSE 8080

CMD python /app/app.py
