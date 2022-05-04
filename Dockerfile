FROM python:3.9

WORKDIR /clound_project
COPY . .

RUN pip3 install -r requirements.txt
ENV FLASK_APP=app/app.py

CMD ["flask", "run"]