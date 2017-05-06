FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.pip /code/
RUN pip install -r requirements.pip
ADD ./src/test_django_api /code/
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh