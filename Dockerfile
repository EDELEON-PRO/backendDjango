# Dockerfile para Django (backend)
# Guarda este archivo como 'Dockerfile' en la carpeta 'backend'
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]