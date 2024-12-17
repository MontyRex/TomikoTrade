FROM python: 3.10.9


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev gettext vim cron locales

RUN useradd -rms /bin/bash tk && chmod 777 /opt /run

WORKDIR /tk

RUN mkdir /tk/static && mkdir /tk/media && chown -R tk:tk /tk && chmod 755 /tk

COPY --chown=tk:tk . .

RUN pip install -r requerments.txt

USER tk

CMD ["manage.py runserver", "-b", "0.0.0.0:8001", "tomiko.wsgi:application"]
