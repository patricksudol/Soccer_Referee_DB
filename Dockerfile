FROM python:3
ENV PYTHONBUFFERED=1
RUN mkdir /Soccer_Referee_DB
WORKDIR /Soccer_Referee_DB
COPY requirements.txt /Soccer_Referee_DB/settings/deps/
RUN pip install -r requirements.txt
COPY . /code/
