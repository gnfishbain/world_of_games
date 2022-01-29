FROM python:3
RUN apt-get update -y
RUN pip install flask
WORKDIR /app
COPY . .
EXPOSE 80
CMD python /app/MainScores.py
