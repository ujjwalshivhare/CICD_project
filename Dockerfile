 FROM redhat/ubi9
RUN yum install -y python3 python3-pip

RUN pip3 install flask
 
COPY app.py /app.py

CMD [ "python3" , "/app.py" ]
