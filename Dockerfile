FROM python:3.13.18-slim

# ENV PYTHON DONT WRITE BYTE CODE=1
ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHON UN BUFFERED=value
ENV PYTHONUNBUFFERED=1

ENV PIP_NO_CACHE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7999

# CMD [ "gunicorn", "library.wsgi:application" , "--bind", "0.0.0.0:8000" ]



CMD ["gunicorn", "library.wsgi:application", \
     "--bind", "0.0.0.0:7999", \
     "--graceful-timeout", "30", \
     "--access-logfile", "-"]
    #    CMD [ "gunicorn", "library.wsgi:application" \
    #    "--bind", "0.0.0.0:8000" \
    #    "--graceful-timeout", "30" \
    #    "--access-logfile", "-"]