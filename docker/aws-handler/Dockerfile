FROM docker.io/library/python:3.11-alpine
WORKDIR /
COPY requirements.txt /
COPY get_role_arn.py /
COPY cloudfront /cloudfront
COPY codedeploy /codedeploy
COPY elasticbeanstalk /elasticbeanstalk
RUN pip install --no-cache-dir -r requirements.txt