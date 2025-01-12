FROM python

WORKDIR /myapp

#COPY ./myapp.py .

#COPY ./servers.txt .

#COPY ./api_demo.py .

COPY ./sql_demo.py .

RUN pip install pymysql

RUN pip install cryptography

CMD ["python", "sql_demo.py"]