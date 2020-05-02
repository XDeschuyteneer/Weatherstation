FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY bridge.py /code/bridge.py
CMD python3 /code/bridge.py