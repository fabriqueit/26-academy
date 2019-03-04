FROM python

ADD _main_.py /
ADD _version.py / 
ADD requirements.txt /

RUN pip install -r requirements.txt
RUN _main_.py -H 10.42.249.158 -P 27017 -D mongo -u mongo -p mongo -A mon_api_bracelet
