FROM python:3.8-alpine3.13
WORKDIR /src
ENV FLASK_APP=myapp.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV PYTHONUNBUFFERED=1
CMD ["flask","run"]
