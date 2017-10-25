FROM    tiangolo/uwsgi-nginx-flask:python2.7
#FROM    python:2.7

FROM	pwierzgala/django-1.8

RUN     pip install django
 
ADD     /requestPortalv6 /app