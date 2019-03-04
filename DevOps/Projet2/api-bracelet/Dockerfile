FROM python

ADD _main_.py
ADD _version.py
ADD requirements.txt

RUN pip install -r requirements.txt
RUN _main_.py -H 0.0.0.0
