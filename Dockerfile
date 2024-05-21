# Instalación de una imagen oficial de Python
FROM python:3.9-slim

# Se establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Se copian los archivos de requerimientos al directorio de trabajo
COPY requirements.txt .

# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Se copian los archivos de la aplicación al directorio de trabajo
COPY . .

# Se ejecutan las migraciones
RUN python manage.py migrate

# Se crea un superusuario
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Se expone el puerto 5000
EXPOSE 5000

# Se ejecuta el comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "descarga_tu_video.wsgi:application"]
