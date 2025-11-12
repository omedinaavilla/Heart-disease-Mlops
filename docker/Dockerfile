# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos desde la carpeta docker
COPY docker/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto (app, etc.) al contenedor
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
