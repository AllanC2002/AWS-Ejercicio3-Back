FROM python:3.9

WORKDIR /app

COPY . .

RUN pip instal -r requirements.txt

EXPOSE 8080

CMD ["Python","main.py"]