FROM python:3.8
RUN mkdir app
WORKDIR /app
COPY /examples /app
RUN pip install flask

EXPOSE 5000
CMD [ "python","flask_ngrok_example.py"]
