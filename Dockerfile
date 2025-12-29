# Image offiviel python:3.13
FROM python:3.13-slim
# defini le repertoire de travail
WORKDIR /app
# installation des dependances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copie les fichiers de l'application
COPY . .
# collect static files
RUN python manage.py collectstatic --noinput
# effectue les migrations de la base de donnees
RUN python manage.py migrate
# Cree un utilisateur non root pour executer l'application
RUN useradd -m myuser
USER myuser
# expose le port 8000
EXPOSE 8000
# demarre l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
