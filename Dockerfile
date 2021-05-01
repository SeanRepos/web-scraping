FROM python:3.8

ADD . /

RUN pip install pipenv

RUN pipenv install

CMD [ "pipenv", "run", "python", "./main.py" ]
