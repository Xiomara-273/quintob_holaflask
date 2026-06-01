# Paso 1 buscar una imagen
FROM python:3.12-alpine

#Paso 2, crear el archivo de trabajo en el contenedor
WORKDIR /app

# Paso 3, copiar el archivo de dependencias
COPY requeriments.txt 

#Paso 4, instalar las dependencias
RUN pip install --no-cache-dir -r requeriments.txt

#Paso 5, copiar el codigo fuente
COPY app.py /app

#Paso 6, exponer el puerto 5000
EXPOSE 5000

#Paso 7, ejecutar la aplicacion 
CMD ["python", "app.py"]