FROM python:alpine3.13 as base

COPY ./requirements.txt /fl/

WORKDIR /fl

RUN apk update && apk add postgresql-dev libpq python3-dev libffi-dev && apk add build-base &&\
apk add libev-dev && mkdir wheels && pip install -r requirements.txt

WORKDIR /root/.cache/pip/wheels

RUN cp ./*/*/*/*/*.whl /fl/wheels

FROM python:alpine3.13

COPY --from=base /fl /fl
COPY app /fl/app
COPY ./config.py /fl/
COPY ./requirements.txt /fl/
COPY ./wsgi.py /fl/

ENV FLASK_APP=app
ENV FLASK_DEBUG=0
#ENV SK
#ENV PSTGR_P
ENV FLASK_CONFIG=/fl/config.py

WORKDIR /fl

RUN pip install --find-links=/fl/wheels -r requirements.txt

EXPOSE 8000

CMD ["gunicorn","--bind=0.0.0.0","-w 4","-k eventlet","wsgi:application"]
