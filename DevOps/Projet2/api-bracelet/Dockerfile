FROM python

ADD __main__.py /
ADD _version.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
RUN /__main__.py -H 0.0.0.0


