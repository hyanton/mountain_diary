FROM python:3.6.1-alpine
WORKDIR /mountain_diary
ADD . /mountain_diary
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "run"]