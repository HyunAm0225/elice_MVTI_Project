FROM python:3.9.0

ENV PYTHONBUFFERED 1

# RUN apt-get update && \
#     apt-get -y install gcc mono-mcs && \
#     rm -rf /var/lib/apt/lists/*

RUN mkdir /django
WORKDIR /django

ADD requirements.txt /django/

RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
RUN python -m textblob.download_corpora


ADD . /django/

RUN python manage.py collectstatic --noinput