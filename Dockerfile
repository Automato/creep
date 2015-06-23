FROM python:3.4.3

RUN mkdir -p /usr/local/creep
WORKDIR /usr/local/creep

COPY requirements.txt /usr/local/creep/
RUN pip install -v -r requirements.txt

COPY . /usr/local/creep
EXPOSE 80

CMD ["python", "./src/creep.py"]
