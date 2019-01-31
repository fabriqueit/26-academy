FROM python:3
ADD requirements.txt /
ADD _version.py /
ADD __main__.py /
RUN pip install -r requirements.txt
CMD [ "python", "./__main__.py", "-H 0.0.0.0", "-P 27017", "-D mongodb", "-u pcolson", "-p 26Academy2018*", "-A 0.0.0.0" ]
