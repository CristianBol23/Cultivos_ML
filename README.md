🌱 Recomendación de cultivosAI

Sistema de recomendación de cultivos basado en Machine Learning que utiliza modelos Random Forest y SVM para predecir el cultivo más adecuado según las características del suelo y condiciones climáticas.


🚀 Descripción del Proyecto

Este proyecto implementa una solución completa de inteligencia artificial que:

Entrena modelos predictivos con scikit-learn

Expone los modelos mediante una API REST usando FastAPI

Despliega el backend en la nube

Consume la API desde un cliente web estático

Permite comparar resultados entre dos modelos distintos


🧠 Modelos Implementados

🌲 Random Forest

Basado en múltiples árboles de decisión

Robusto ante ruido

Buena generalización


📈 Support Vector Machine (SVM)

Basado en hiperplanos de separación

Requiere normalización de datos


📊 Dataset

Se utilizó el dataset Crop Recommendation, el cual contiene variables como:

N (Nitrógeno)

P (Fósforo)

K (Potasio)

Temperatura

Humedad

pH

Lluvia


⚙️ Tecnologías Utilizadas

Python

scikit-learn

FastAPI

Pydantic

Uvicorn / Gunicorn

NumPy

HTML, CSS, JavaScript

Render (deploy)


🏗️ Arquitectura del Proyecto

project/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── schemas/
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md


🔌 API REST

Endpoint Random Forest

POST /predict/rf

Endpoint SVM

POST /predict/svm


📥 Ejemplo de Entrada

{

  "N": 90,
  
  "P": 40,
  
  "K": 40,
  
  "temperature": 22,
  
  "humidity": 85,
  
  "ph": 6.5,
  
  "rainfall": 200
  
}


📤 Ejemplo de Salida
{
  "prediction": "Arroz"
}
🌐 Cliente Web

Se desarrolló un cliente web estático que permite:

Ingresar datos del suelo
Seleccionar modelo (RF o SVM)
Realizar predicción
Visualizar resultados en tiempo real
🎨 Características del Frontend
Interfaz moderna con CSS
Gradientes animados
Validación de datos
Manejo de errores
Consumo de API con Fetch
🔄 Flujo del Sistema
Usuario ingresa datos en la web
Se envía una petición POST al backend
FastAPI recibe y valida datos con Pydantic
Se procesa con el modelo seleccionado
Se retorna la predicción
El frontend muestra el resultado
🌍 Despliegue

El backend fue desplegado en Render:

Configuración de entorno
Uso de $PORT
Manejo de CORS
Integración continua con GitHub
⚠️ Problemas Resueltos

Durante el desarrollo se solucionaron:

Errores de CORS
Problemas de rutas (404)
Manejo de puertos en producción
Errores de serialización
Cache del navegador
Estructura de respuesta JSON
🌎 Traducción de Resultados

Se implementó un sistema de traducción para convertir las salidas del modelo de inglés a español, mejorando la experiencia del usuario.

🧠 Consideraciones Importantes
Es normal que los modelos (RF y SVM) den resultados diferentes
Esto se debe a sus distintos enfoques matemáticos
Permite comparar rendimiento y comportamiento
🧪 Pruebas

Se realizaron pruebas con diferentes combinaciones de variables para validar:

Precisión del modelo
Respuesta del sistema
Diferencias entre algoritmos
📦 Instalación Local
conda create -n cultivos_env
conda activate cultivos_env
pip install -r requirements.txt
uvicorn main:app --reload
👨‍💻 Autor

Proyecto desarrollado como parte del curso de Modelos Predictivos

📌 Conclusión

Se logró implementar una solución completa de machine learning aplicada, integrando:

Entrenamiento de modelos
Desarrollo de API
Consumo desde frontend
Despliegue en la nube
