FROM    tiangolo/uwsgi-nginx-flask:python2.7

FROM	pwierzgala/django-1.8

RUN		 pip install --upgrade pip

RUN     pip install django

ADD     /requestPortalv6 /requestPortalv6

RUN pip install -r /requestPortalv6/requirements.txt

EXPOSE 3000

WORKDIR /requestPortalv6

CMD 	python manage.py runserver
