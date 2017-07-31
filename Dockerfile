FROM python:3.6.1-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk update
RUN mkdir -p ~/.pip;\
    echo [global] > ~/.pip/pip.conf;\
    echo index-url = http://mirrors.aliyun.com/pypi/simple/ >> ~/.pip/pip.conf;\
    echo [install] >> ~/.pip/pip.conf;\
    echo trusted-host=mirrors.aliyun.com >> ~/.pip/pip.conf;\
    pip install gunicorn

ADD . /mysite
WORKDIR /mysite
RUN pip install -r requirement.txt
CMD gunicorn --config file:gunicorn.conf.py --bind=0.0.0.0:5000 manage



