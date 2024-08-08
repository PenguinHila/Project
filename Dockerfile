FROM python:alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main_score.py .
EXPOSE 8777
CMD python main_score.py
