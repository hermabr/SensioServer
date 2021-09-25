FROM python:3.9

RUN groupadd -r sensiobruker && useradd -r -s /bin/false -g sensiobruker sensiobruker

COPY requirements.txt /www/requirements.txt
WORKDIR /www
RUN pip install -r requirements.txt
COPY . /www

RUN chown -R sensiobruker:sensiobruker /www
USER sensiobruker

#CMD python app.py
CMD ["python","-u","run.py"]
