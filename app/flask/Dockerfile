FROM python:3.7

ENV PORT=8080
WORKDIR /usr/src/app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app