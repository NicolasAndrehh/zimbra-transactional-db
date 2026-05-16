# Sistema Transaccional Zimbra

Transactional system for Zimbra's sales and marketing processes. Built with React, Python, and MySQL.

Este proyecto ha sido desarrollado como parte de la asignatura de **Sistemas Transaccionales** en **UNIMINUTO**.

### 👥 Integrantes del Equipo
* Barragan España James Steven
* Olaya Gamba Nicolás Andrés
* Pico Paez Ana María

**Tutor:** Ladi Paola Ballen Carrasco  
**Institución:** Corporación Universitaria Minuto de Dios (UNIMINUTO)  
**Sede:** Bogotá D.C.

---

## 🛠️ Tecnologías Utilizadas

* **Frontend:** React.js (generado con Vite)
* **Backend:** Python (Flask, Flask-CORS)
* **Base de Datos:** MySQL (mysql-connector-python)

---

## 📂 Estructura del Proyecto

```text
zimbra-transactional-db/
├── backend/            # Servidor API en Python/Flask
│   ├── app.py          # Punto de entrada de la API
│   ├── requirements.txt# Dependencias de Python
│   └── venv/           # Entorno virtual (Ignorado en Git)
├── frontend/           # Interfaz de usuario en React
│   ├── package.json    # Configuración de Node
│   └── node_modules/   # Dependencias de Node (Ignorado en Git)
├── bd/                 # Scripts de base de datos
│   └── schema.sql      # Estructura del modelo Entidad-Relación
└── .gitignore          # Archivo de exclusión de Git
```

---

## 🚀 Instrucciones de Configuración e Instalación

Para trabajar en este repositorio localmente, sigue estos pasos en estricto orden:

### 1️⃣ Clonar el Repositorio
Abre tu terminal y descarga el proyecto en tu máquina local:

```bash
git clone [https://github.com/TU-USUARIO/zimbra-transactional-db.git](https://github.com/TU-USUARIO/zimbra-transactional-db.git)
cd zimbra-transactional-db
```

### 2️⃣ Configurar la Base de Datos (MySQL)
1. Abre tu gestor de base de datos local (XAMPP, MySQL Workbench, WAMP, etc.).
2. Asegúrate de que el servicio de MySQL esté encendido y corriendo.
3. Importa y ejecuta el script ubicado en la ruta `bd/schema.sql`. Esto creará la base de datos `zimbra_db` y todas sus tablas estructuradas.

### 3️⃣ Configurar y Ejecutar el Backend (Python + Flask)
Abre una terminal en la **raíz del proyecto** y ejecuta los siguientes comandos línea por línea:

```bash
cd backend

# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual (En Windows)
.\venv\Scripts\activate

# 3. Instalar las dependencias necesarias
pip install -r requirements.txt

# 4. Iniciar el servidor de desarrollo
python app.py
```
> **📍 Nota:** Si todo salió bien, el backend quedará corriendo en: `http://localhost:5000`

### 4️⃣ Configurar y Ejecutar el Frontend (React + Vite)
Abre **otra terminal diferente** (no cierres la del backend) en la raíz del proyecto y ejecuta:

```bash
cd frontend

# 1. Instalar los paquetes de Node.js (Recrea la carpeta node_modules)
npm install

# 2. Iniciar el servidor frontend de Vite
npm run dev
```
> **📍 Nota:** El frontend quedará corriendo y listo para visualizarse en: `http://localhost:5173`

---

## 🔒 Buenas Prácticas del Repositorio

* **⚠️ ¡NUNCA subas `node_modules/` ni `venv/` a GitHub!** Ya están configurados en el archivo `.gitignore` para ser bloqueados.
* Si instalas una **nueva dependencia en Python** para el backend, es obligatorio actualizar el listado para el resto del equipo. Ve a la terminal del backend (con el entorno activo) y ejecuta:

```bash
pip freeze > requirements.txt
```
