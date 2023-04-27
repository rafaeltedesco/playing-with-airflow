FROM python:3.10

WORKDIR /usr/application/teste

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python src/main.py

