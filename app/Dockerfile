FROM nikolaik/python-nodejs:latest

ENV PYTHONUNBUFFERED 1

ADD ./src/ /code
ADD ./uwsgi /uwsgi
WORKDIR /code
ADD *requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt; \
 python manage.py collectstatic
EXPOSE 8080
CMD uwsgi --ini /uwsgi/conf/develop.ini