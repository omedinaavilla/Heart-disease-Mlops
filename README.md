# Heart Disease Prediction — MLOps Project  

 *Implementación completa de un flujo MLOps local con FastAPI, Docker, Kubernetes y GitHub Actions.*

---

##  Descripción General  

Este proyecto aplica prácticas modernas de **Machine Learning Operations (MLOps)** para entrenar, versionar y desplegar un modelo que predice el riesgo de enfermedad cardíaca a partir de variables clínicas.  

Incluye todo el ciclo de vida de un modelo de ML: desde el análisis exploratorio (EDA) hasta el despliegue automatizado mediante contenedores y orquestación local.  

---

##  Estructura del Proyecto  
``` 



heart-disease-mlops/
│── data/
│   └── heart.csv                 # Dataset original (EDA)
│
│── notebooks/
│   ├── 1_data_leakage.ipynb      # Análisis de fuga de datos (data leakage)
│   └── 2_model_training.ipynb    # Entrenamiento y evaluación de modelos
│
│── models/
│   └── logistic_regression_final.joblib   # Modelo final entrenado y exportado
│
│── app/
│   ├── api.py                    # API principal FastAPI
│   └── __init__.py
│
│── docker/
│   ├── Dockerfile                # Imagen Docker de la aplicación
│   └── requirements.txt          # Dependencias del proyecto
│
│── k8s/
│   ├── deployment.yaml           # Despliegue del contenedor (Kubernetes)
│   └── service.yaml              # Servicio LoadBalancer
│
└── .github/
    └── workflows/
        └── deploy.yml            # Pipeline CI/CD (GitHub Actions)
``` 

---

##  Tecnologías Empleadas  

|  Herramienta |  Descripción |
|----------------|----------------|
| **Python 3.11** | Lenguaje principal del proyecto |
| **FastAPI** | Framework para la creación de la API REST del modelo |
| **scikit-learn** | Entrenamiento, evaluación y validación del modelo de ML |
| **Joblib** | Serialización y carga del modelo entrenado |
| **Uvicorn** | Servidor ASGI utilizado para desplegar la API |
| **Docker** | Contenerización de la aplicación |
| **Kubernetes (Minikube / Docker Desktop)** | Orquestación de contenedores local |
| **GitHub Actions** | Automatización del pipeline de CI/CD |
``` 
---

##  Componentes Clave  

###  1. Exploratory Data Analysis (EDA)  
- Limpieza y preprocesamiento del dataset.  
- Análisis de correlaciones y detección de *data leakage*.  

###  2. Entrenamiento del Modelo  
- Modelos probados:  
  - Logistic Regression  
  - Random Forest  
  - K-Nearest Neighbors  
  - Gradient Boosting  
- Selección final: **Logistic Regression**, por su interpretabilidad y mejor recall en contextos médicos.

###  3. API con FastAPI  
- Endpoint principal: `/predict`  
- Interfaz Swagger en `/docs`  
- Predicciones rápidas a partir de datos JSON de pacientes.

### 4. Dockerización  
- `Dockerfile` define el entorno reproducible con dependencias exactas.  
- Permite ejecutar la API localmente en contenedor.

### 5. Despliegue con Kubernetes  
- `deployment.yaml`: gestiona el pod con la imagen Docker.  
- `service.yaml`: expone la API vía LoadBalancer (accesible desde el navegador).  

### 6. CI/CD con GitHub Actions  
- Construcción automática de la imagen Docker.  
- Publicación en DockerHub.  
- Despliegue en Kubernetes tras cada *push* a la rama `main`.  

---

## Ejecución Local  

###  1. Crear entorno e instalar dependencias
```bash
conda create -n ml_venv python=3.11
conda activate ml_venv
pip install -r docker/requirements.txt

uvicorn app.api:app --reload

docker build -t heart-disease-api -f docker/Dockerfile .
docker run -p 8000:8000 heart-disease-api

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc

Link creado para ejecutar localmente: 
http://localhost:<PUERTO_EXTERNO>/docs

