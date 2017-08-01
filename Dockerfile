FROM python:3
RUN pip install gunicorn -i "http://mirrors.aliyun.com/pypi/simple/" --trusted-host "mirrors.aliyun.com"
ADD requirement.txt /requirement.txt
RUN pip install -i "http://mirrors.aliyun.com/pypi/simple/" --trusted-host "mirrors.aliyun.com" -r /requirement.txt
ADD . /mysite
WORKDIR /mysite
CMD ["gunicorn","--config", "file:gunicorn.conf.py" "--bind=0.0.0.0:5001", "mysite.wsgi:application"]



