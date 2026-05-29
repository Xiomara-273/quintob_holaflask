# 
FROM python :3.12-alpine

#Paso 2 
WORKDIR /app

# Paso 3
COPY requeriments.txt 

#Paso 4 
RUN pip install --no-cache-dir -r requeriments.txt

#Paso 5 
COPY app.py /app

#Paso 6
EXPOSE 5000

#Paso 7 ejecutar laaplicacion 
CMD ["python", "app.py"]