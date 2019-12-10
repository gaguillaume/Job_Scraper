FROM python:3.6

RUN mkdir /home/dev/ && mkdir /home/dev/app

WORKDIR /home/dev/code

COPY . /home/dev/code/app

WORKDIR /home/dev/code/app

RUN echo $(ls -l .)

RUN pip install --upgrade pip && pip install pipenv && pipenv install --skip-lock

CMD ["pipenv", "run", "python", "run.py"]
