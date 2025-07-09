# 🧠 Task Manager API

¡Bienvenido a Task Manager API! 🧩
Una API RESTful construida con FastAPI para gestionar tareas de manera eficiente, segura y escalable
Construida en proceso de aprendizaje de lenguaje Python.

# 🧱 Estructura del Proyecto
task_manager_api/
├── config/           # Configuraciones del proyecto
├── db/               # Configuración y conexión a la base de datos
├── models/           # Modelos ORM
├── routers/          # Rutas de la API
├── schemas/          # Esquemas de Pydantic
├── services/         # Lógica de negocio
├── utils/            # Utilidades y funciones auxiliares
├── main.py           # Punto de entrada de la aplicación
├── requirements.txt  # Dependencias del proyecto
└── .env.example      # Variables de entorno de ejemplo


## Crea un entorno virtual e instala las dependencias:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

## Configura las variables de entorno:
Copia el archivo .env.example a .env y ajusta los valores según tu entorno.

## Inicia la aplicación:
uvicorn main:app --reload


## Accede a la documentación interactiva:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
