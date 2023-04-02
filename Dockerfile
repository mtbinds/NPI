FROM python:3.10.0-alpine
WORKDIR /app
ENV FLASK_APP=NPI.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
# Nous permets d'utiliser le serveur (waitress) qui est un serveur de production
CMD ["python","NPI.py" ]

