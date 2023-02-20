FROM python:alpine
COPY app /usr/share/app
WORKDIR /usr/share/app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD [ "python3", "app.py"]
