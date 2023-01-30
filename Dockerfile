FROM python:3.11-alpine
WORKDIR /myblog
COPY ./ /myblog
RUN apk update && pip install -r /myblog/requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
