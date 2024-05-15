# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

#
ARG SSL_KEY_PATH
ARG SSL_CERT_PATH

#
ENV SSL_KEY_PATH=$SSL_KEY_PATH
ENV SSL_KEY_PATH=$SSL_CERT_PATH

# 
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 80 --ssl-keyfile ${SSL_KEY_PATH} --ssl-certfile ${SSL_CERT_PATH}