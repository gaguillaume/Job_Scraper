FROM python:3.6

RUN mkdir /home/dev/ && mkdir /home/dev/code

WORKDIR /home/dev/code

COPY  . /home/dev/code/

WORKDIR /home/dev/code/


RUN pip install --upgrade pip && pip install pipenv && pipenv install --skip-lock


RUN echo $(ls -l .)


CMD ["pipenv", "run", "python", "run.py"]
