FROM python:3.8.5
WORKDIR /app
RUN python -m pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]