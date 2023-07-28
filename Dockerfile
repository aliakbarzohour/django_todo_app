FROM python:3.9

WORKDIR ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 manage.py runserver