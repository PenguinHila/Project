FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN git clone https://github.com/PenguinHila/Project.git .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8777
EXPOSE 5000
PUBLISH 8777:5000
CMD python main_score.py
