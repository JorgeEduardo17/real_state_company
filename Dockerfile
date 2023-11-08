# Utiliza la imagen base oficial de Python
FROM python:3.11.5-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Crea el directorio /images y asigna los permisos adecuados
#RUN mkdir -p /app/images && chmod 755 /app/images

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Indica el comando predeterminado para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]