FROM python
ADD __main__.py /
ADD _version.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
RUN chmod u+x __main__.py
CMD /__main__.py -H 10.42.249.158 -P 27017 -D APIconsume-mongo-1 -u mongo -p mongo -A mon_api_bracelet
