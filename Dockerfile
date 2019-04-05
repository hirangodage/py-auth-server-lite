FROM python:alpine
RUN mkdir -p /var/auth-server
COPY ./ /var/auth-server
RUN pip install -r /var/auth-server/requirements.txt
ENTRYPOINT python /var/auth-server/WebServer.py
EXPOSE 8088