# Paso 1: buscar una imagen
FROM python:3.12-alpine

# Paso 2: crear el archivo de trabajo en el contenedor
WORKDIR /app

# Paso 3: copiar el archivo de dependencias (se agrega el espacio y el punto al final)
COPY requirements.txt .

# Paso 4: instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Paso 5: copiar el codigo fuente (usamos el punto . porque ya estamos en /app)
COPY app.py .

# Paso 6: exponer el puerto 5000
EXPOSE 5000

# Paso 7: ejecutar la aplicacion 
CMD ["python", "app.py"]