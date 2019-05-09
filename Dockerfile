FROM tiangolo/uwsgi-nginx:python3.7

WORKDIR /app

COPY . /app

RUN set -xe \
    && apt update \
    && apt install gcc -y \
    && apt install python3-dev -y \
    && pip3 install -r requirements.txt

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000

CMD ["python3", "manage.py", "migrate"]