FROM python:3.4.3

RUN mkdir -p /usr/local/creep
WORKDIR /usr/local/creep

COPY requirements.txt /usr/local/creep/
RUN pip install -v -r requirements.txt

EXPOSE 80
COPY . /usr/local/creep

CMD ["python", "./src/creep.py"]
