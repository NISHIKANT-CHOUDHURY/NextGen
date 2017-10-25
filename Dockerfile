FROM    tiangolo/uwsgi-nginx-flask:python2.7

FROM	pwierzgala/django-1.8

RUN     pip install django
 
ADD     /requestPortalv6 /app

CMD 	python manage.py runserver 3000
