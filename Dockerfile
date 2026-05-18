FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y 
#updating all the packages before doing the deployment

RUN pip install -r requirements.txt
CMD ["python3", "application.py"]