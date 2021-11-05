FROM python:3.7
WORKDIR .
RUN python -m pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN python -m pip  install -r requirements.txt
RUN python -m pip install -r requirements.txt
RUN mkdir sandbox
RUN touch script.py
RUN touch db.txt