FROM python:3
ADD . /mysite
WORKDIR /mysite
RUN pip install gunicorn -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirement.txt
CMD ["gunicorn","--config", "file:gunicorn.conf.py" "--bind=0.0.0.0:5001", "mysite.wsgi:application"]



