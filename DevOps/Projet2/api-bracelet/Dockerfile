FROM python

ADD _main_.py
ADD _version.py
ADD requirements.txt

RUN pip install -r requirements.txt
RUN \_\_main\_\_.py -H 0.0.0.0
