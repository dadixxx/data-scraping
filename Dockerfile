FROM python:latest
COPY . .
CMD python 4_parse_js.py

RUN pip3 install --no-cache-dir -r requirements.txt

