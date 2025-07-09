# 🧠 Task Manager API

¡Bienvenido a **Task Manager API**! 🧩  
Una API RESTful construida con [FastAPI](https://fastapi.tiangolo.com/) para gestionar tareas de manera eficiente, segura y escalable.  
> ⚠️ Este proyecto está siendo desarrollado como parte de mi proceso de aprendizaje en Python y FastAPI.

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/mfacuna/task_manager_api.git
cd task_manager_api


### 2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Configura las variables de entorno:
Copia el archivo .env.example a .env y ajusta los valores según tu entorno.

### 4. Inicia la aplicación:
```bash
uvicorn main:app --reload


## Accede a la documentación interactiva:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
