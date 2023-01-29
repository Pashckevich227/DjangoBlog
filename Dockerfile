FROM python:3.11-alpine
WORKDIR /django_blog
COPY ./ /myblog
RUN apk update && pip install -r /myblog/requirements.txt --no-cache-dir
EXPOSE 8000
CWD ["python", "manage.py", "runserver"]
